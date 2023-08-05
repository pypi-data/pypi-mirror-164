# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed
#  without the express permission of Comet ML Inc.
# *******************************************************

import json
import logging
from threading import RLock

import six

from ._typing import Any, Callable, Dict, List, Optional
from .messages import BaseMessage, ParameterMessage, RemoteAssetMessage
from .utils import compact_json_dump, get_time_monotonic

LOGGER = logging.getLogger(__name__)


class Batch(object):
    """
    The Batch object contains a list of anything and manage the size of the batch, isolating the
    logic about the max size and max time for a batch
    """

    def __init__(self, max_batch_size, max_batch_time):
        self.batch = []  # type: List[Any]
        self.on_upload_callbacks = []  # type: List[Any]
        self.last_time_created = get_time_monotonic()

        self.max_batch_size = max_batch_size
        self.max_batch_time = max_batch_time

    def _append(self, batch_item, on_upload=None):
        # type: (Any, Any) -> None
        if len(self.batch) == 0:
            self.last_time_created = get_time_monotonic()

        self.batch.append(batch_item)

        if on_upload is not None:
            self.on_upload_callbacks.append(on_upload)

    def __len__(self):
        return len(self.batch)

    def should_be_uploaded(self):
        # type: () -> bool
        if len(self.batch) == 0:
            return False

        duration_since_last_created = get_time_monotonic() - self.last_time_created

        return (
            len(self.batch) >= self.max_batch_size
            or duration_since_last_created >= self.max_batch_time
        )

    def get_and_clear(self):
        # type: () -> List[Any]
        batch = self.batch
        self.clear()
        return batch

    def clear(self):
        self.batch = []

    def _get_payload(self):
        return self.batch

    def call_on_upload(self, *args, **kwargs):
        for callback in self.on_upload_callbacks:
            try:
                callback(*args, **kwargs)
            except Exception:
                LOGGER.debug(
                    "Error calling on_upload callback from a batch", exc_info=True
                )


class RemoteAssetsBatch(Batch):
    def append(self, remote_asset_message, additional_data=None, on_upload=None):
        # type: (RemoteAssetMessage, Optional[Dict[str, Any]], Any) -> None
        batch_item = {
            "assetId": remote_asset_message.additional_params["assetId"],
            "fileName": remote_asset_message.additional_params["fileName"],
            "link": remote_asset_message.remote_uri,
            "metadata": json.dumps(remote_asset_message.metadata),
            "overwrite": remote_asset_message.additional_params["overwrite"],
        }

        if remote_asset_message.additional_params.get("type") is not None:
            batch_item["type"] = remote_asset_message.additional_params["type"]

        if remote_asset_message.additional_params.get("step") is not None:
            batch_item["step"] = remote_asset_message.additional_params["step"]

        if remote_asset_message.additional_params.get("artifactVersionId") is not None:
            batch_item["artifactVersionId"] = remote_asset_message.additional_params[
                "artifactVersionId"
            ]

        if additional_data is not None:
            batch_item.update(additional_data)

        super(RemoteAssetsBatch, self)._append(batch_item, on_upload=on_upload)

    def get_payload(self):
        # type: () -> six.BytesIO
        payload = six.BytesIO()
        compact_json_dump({"remoteAssets": self.batch}, payload)
        return payload


class ParametersBatch(object):
    """The batch object to maintain schedule of parameters sending."""

    def __init__(self, base_interval):
        # type: (float) -> None
        """Creates new instance of parameters batch. The base_interval value will be used as initial interval
        between accept events and will be incremented with values generated by backoff_gen each time new message
        was accepted.

        Args:
            base_interval:
                The base interval between sending collected parameters
        """
        self.base_interval = base_interval
        self.last_time = 0.0
        self.items = {}  # type: Dict[str, MessageBatchItem]
        # the lock to make sure that ready_to_accept and accept public methods are synchronized
        # and implementation is thread safe
        self.lock = RLock()

    def empty(self):
        # type: () -> bool
        """Allows to check if this batch is empty"""
        return len(self.items) == 0

    def append(self, message, offset):
        # type: (ParameterMessage, int) -> bool
        """Appends specified message to the collection of messages maintained by this batch.

        Args:
            message:
                The message to be accepted or ignored
            offset:
                The message offset in the queue

        Returns:
            True if specified message was accepted by this batch.
        """
        if not isinstance(message, ParameterMessage):
            return False

        name = message.get_param_name()
        if name is None or name == "":
            # empty message
            return False

        # include context if present
        if message.context is not None:
            name = "%s_%s" % (message.context, name)

        self.items[name] = MessageBatchItem(message, offset)
        return True

    def accept(self, callback, unconditional=False):
        # type: (Callable[List[MessageBatchItem], None], bool) -> bool
        """Accepts or ignores provided callback depending on last time this method was invoked and current interval
        between accept events. If time elapsed since last accept exceeds base_interval the provided callback will
        be used to send all collected parameters and batch state will be cleaned.

        Args:
            callback:
                The callback function to be invoked with message, offset as argument if it was accepted.
            unconditional:
                The flag to indicate if  callback should be accepted unconditionally if there are items to be processed.
        Returns:
            True if callback was accepted and all parameters was sent.
        Raises:
            ValueError: is callback is None
        """
        if callback is None:
            raise ValueError("Callback is None")

        with self.lock:
            if self.ready_to_accept(unconditional):
                self._accept(callback)
                return True
            else:
                return False

    def ready_to_accept(self, unconditional=False):
        # type: (bool) -> bool
        """Method to check if this batch is ready to accept the next callback

        Args:
            unconditional:
                The flag to indicate if  callback should be accepted unconditionally if there are items to be processed.
        Returns:
            True if next callback will be accepted.
        """
        with self.lock:
            if self.empty():
                return False

            if self.last_time == 0 or unconditional:
                return True

            duration_since_last_time = get_time_monotonic() - self.last_time
            return duration_since_last_time >= self.base_interval

    def update_interval(self, interval):
        # type: (float) -> None
        """The callback method invoked to update the interval between batch processing

        Args:
            interval:
                The new interval value in seconds.
        """
        with self.lock:
            self.base_interval = interval

    def _accept(self, callback):
        # type: (Callable[List[MessageBatchItem], None]) -> None
        """Accepts the specified callback for all parameters collected so forth"""
        with self.lock:
            keys = list(self.items.keys())
            list_to_sent = list()
            for key in keys:
                list_to_sent.append(self.items[key])
                self.items.pop(key)

        # send batch
        try:
            callback(list_to_sent)
        except Exception:
            LOGGER.debug("Failed to send parameters batch", exc_info=True)

        self.last_time = get_time_monotonic()


class MessageBatchItem(object):
    """Represents batch item holding specific message and offset associated with it."""

    __slots__ = ("message", "offset")

    def __init__(self, message, offset=None):
        # type: (BaseMessage, Optional[int]) -> None
        self.message = message
        self.offset = offset


class MessageBatch(object):
    """The batch object to maintain list of messages to be sent constrained by size and interval between send events."""

    def __init__(self, base_interval, max_size):
        # type: (float, int) -> None
        """Creates new instance of batch. The base_interval value will be used as initial interval
        between accept events and will be incremented with values generated by backoff_gen each time new message
        was accepted. Also, it would check the current number of collected messages against max_size when new message
        accepted by the batch. When number of collected values exceeds max_size the collected  messages will be sent
        immediately.


        Args:
            base_interval:
                The base interval between sending collected message.
            max_size:
                The maximal size of collected message to be kept.
        """
        self.base_interval = base_interval
        self.max_size = max_size
        self.last_time = 0.0
        self.items = list()  # type: List[MessageBatchItem]
        # the lock to make sure that ready_to_accept and accept public methods are synchronized
        # and implementation is thread safe
        self.lock = RLock()

    def empty(self):
        # type: () -> bool
        """Allows to check if this batch is empty"""
        return len(self.items) == 0

    def update_interval(self, interval):
        # type: (float) -> None
        """The callback method invoked to update the interval between batch processing

        Args:
            interval:
                The new interval value in seconds.
        """
        with self.lock:
            self.base_interval = interval

    def append(self, message, offset=None):
        # type: (BaseMessage, Optional[int]) -> None
        """Appends specified message to the collection of messages maintained by this batch.

        Args:
            message:
                The message to be accepted or ignored
            offset:
                The message offset in the queue
        """
        assert isinstance(message, BaseMessage)

        self.items.append(MessageBatchItem(message=message, offset=offset))

    def accept(self, callback, unconditional=False):
        # type: (Callable[List[MessageBatchItem], None], bool) -> bool
        """Accepts or ignores provided callback depending on last time this method was invoked and current interval
        between accept events. If time elapsed since last accept exceeds base_interval the provided callback will
        be used to send all collected messages and batch state will be cleaned. Also, if number of collected
        messages equals or greater than max_size the callback will be accepted.

        Args:
            callback:
                The callback function to be invoked with list of batch items as argument if it is accepted.
            unconditional:
                The flag to indicate if callback should be accepted unconditionally if there are items to be processed.
        Returns:
            True if callback was accepted and all collected messages was successfully sent.
        Raises:
            ValueError: is callback is None
        """
        if callback is None:
            raise ValueError("Callback is None")

        with self.lock:
            if self._ready_to_accept(unconditional):
                return self._accept(callback)
            else:
                return False

    def _ready_to_accept(self, unconditional=False):
        # type: (bool) -> bool
        """Method to check if this batch is ready to accept the next callback.

        Args:
            unconditional:
                The flag to indicate if  callback should be accepted unconditionally if there are items to be processed.
        Returns:
            True if next callback will be accepted.
        """
        with self.lock:
            if self.empty():
                return False

            if self.last_time == 0 or unconditional:
                return True

            duration_since_last_time = get_time_monotonic() - self.last_time
            if duration_since_last_time >= self.base_interval:
                return True

            return len(self.items) >= self.max_size

    def _accept(self, callback):
        # type: (Callable[List[MessageBatchItem], None]) -> bool
        """Accepts the specified callback for all items collected so forth"""
        with self.lock:
            # copy items to new list to avoid list changes while sending due to appending new items
            list_to_sent = self.items
            self.items = list()

        successful = False
        try:
            callback(list_to_sent)
            successful = True
        except Exception:
            LOGGER.debug("Failed to send messages batch", exc_info=True)

        self.last_time = get_time_monotonic()
        return successful

#
# Copyright (c) 2021 Nitric Technologies Pty Ltd.
#
# This file is part of Nitric Python 3 SDK.
# See https://github.com/nitrictech/python-sdk for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import Any, List, Optional, Union

from grpclib import GRPCError
from grpclib.client import Channel

from nitric.exception import exception_from_grpc_error, InvalidArgumentException
from nitric.utils import new_default_channel, struct_from_dict, dict_from_struct
from nitric.proto.nitric.queue.v1 import (
    QueueServiceStub,
    NitricTask,
    FailedTask as WireFailedTask,
    QueueCompleteRequest,
    QueueSendRequest,
    QueueSendBatchRequest,
    QueueReceiveRequest,
)
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Task(object):
    """A task to be sent to a Queue."""

    id: Optional[str] = field(default=None)
    payload_type: Optional[str] = field(default=None)
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, order=True)
class ReceivedTask(object):
    """A reference to a task received from a Queue, with a lease."""

    lease_id: str = field()
    _queueing: Queues = field()
    _queue: QueueRef = field()
    id: Optional[str] = field(default=None)
    payload_type: Optional[str] = field(default=None)
    payload: dict[str, Any] = field(default_factory=dict)

    async def complete(self):
        """
        Mark this task as complete and remove it from the queue.

        Only callable for tasks that have been received from a Queue.
        """
        try:
            await self._queueing.queue_stub.complete(
                queue_complete_request=QueueCompleteRequest(queue=self._queue.name, lease_id=self.lease_id)
            )
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)


@dataclass(frozen=True, order=True)
class FailedTask(Task):
    """Represents a failed queue publish."""

    message: str = field(default="")


def _task_to_wire(task: Task) -> NitricTask:
    """
    Convert a Nitric Task to a Nitric Queue Task.

    :param task: to convert
    :return: converted task
    """
    return NitricTask(
        id=task.id if task.id else None,
        payload_type=task.payload_type if task.payload_type else None,
        payload=struct_from_dict(task.payload),
    )


def _wire_to_received_task(task: NitricTask, queueing: Queues, queue: QueueRef) -> ReceivedTask:
    """
    Convert a Nitric Queue Task (protobuf) to a Nitric Task (python SDK).

    :param task: to convert
    :return: converted task
    """
    return ReceivedTask(
        id=task.id,
        payload_type=task.payload_type,
        payload=dict_from_struct(task.payload),
        lease_id=task.lease_id,
        _queueing=queueing,
        _queue=queue,
    )


def _wire_to_failed_task(failed_task: WireFailedTask) -> FailedTask:
    """
    Convert a queue task that failed to push into a Failed Task object.

    :param failed_task: the failed task
    :return: the Failed Task with failure message
    """
    return FailedTask(
        id=failed_task.task.id,
        payload_type=failed_task.task.payload_type,
        payload=dict_from_struct(failed_task.task.payload),
        message=failed_task.message,
    )


@dataclass(frozen=True, order=True)
class QueueRef(object):
    """A reference to a queue from a queue service, used to perform operations on that queue."""

    _queueing: Queues
    name: str

    async def send(
        self, tasks: Union[Task, dict[str, Any], List[Union[Task, dict[str, Any]]]]
    ) -> Union[None, Task, List[FailedTask]]:
        """
        Send one or more tasks to this queue.

        If a list of tasks is provided this function will return a list containing any tasks that failed to be sent to
        the queue.

        :param tasks: A task or list of tasks to send to the queue.
        """
        if isinstance(tasks, list):
            return await self._send_batch(tasks)

        task = tasks

        if isinstance(task, dict):
            # Handle if its just a payload
            if task.get("payload") is None:
                task = {"payload": task}
            task = Task(**task)

        try:
            await self._queueing.queue_stub.send(
                queue_send_request=QueueSendRequest(queue=self.name, task=_task_to_wire(task))
            )
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)

    async def _send_batch(
        self, tasks: List[Union[Task, dict[str, Any]]], raise_on_failure: bool = True
    ) -> List[FailedTask]:
        """
        Push a collection of tasks to a queue, which can be retrieved by other services.

        :param tasks: The tasks to push to the queue
        :param raise_on_failure: Whether to raise an exception when one or more tasks fails to send
        :return: PushResponse containing a list containing details of any messages that failed to publish.
        """
        if len(tasks) < 1:
            raise InvalidArgumentException("No tasks provided, nothing to send.")

        wire_tasks = [_task_to_wire(Task(**task) if isinstance(task, dict) else task) for task in tasks]

        try:
            response = await self._queueing.queue_stub.send_batch(
                queue_send_batch_request=QueueSendBatchRequest(queue=self.name, tasks=wire_tasks)
            )
            return [_wire_to_failed_task(failed_task) for failed_task in response.failed_tasks]
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)

    async def receive(self, limit: Optional[int] = None) -> List[ReceivedTask]:
        """
        Pop 1 or more items from the specified queue up to the depth limit.

        Queue items are Nitric Tasks that are leased for a limited period of time, where they may be worked on.
        Once complete or failed they must be acknowledged using the request specific leaseId.

        If the lease on a queue item expires before it is acknowledged or the lease is extended the task will be
        returned to the queue for reprocessing.

        :param limit: The maximum number of queue items to return. Default: 1, Min: 1.
        :return: Queue items popped from the specified queue.
        """
        # Set the default and minimum depth to 1.
        if limit is None or limit < 1:
            limit = 1

        try:
            response = await self._queueing.queue_stub.receive(
                queue_receive_request=QueueReceiveRequest(queue=self.name, depth=limit)
            )
            # Map the response protobuf response items to Python SDK Nitric Tasks
            return [_wire_to_received_task(task=task, queueing=self._queueing, queue=self) for task in response.tasks]
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)


class Queues(object):
    """Queueing client, providing access to Queue and Task references and operations on those entities."""

    def __init__(self):
        """Construct a Nitric Queue Client."""
        self.channel: Union[Channel, None] = new_default_channel()
        self.queue_stub = QueueServiceStub(channel=self.channel)

    def __del__(self):
        # close the channel when this client is destroyed
        if self.channel is not None:
            self.channel.close()

    def queue(self, name: str):
        """Return a reference to a queue from the connected queue service."""
        return QueueRef(_queueing=self, name=name)

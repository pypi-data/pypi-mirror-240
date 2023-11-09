"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The MIT License

Copyright (c) 2020 Temporal Technologies Inc.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.task_queue_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TaskQueue(google.protobuf.message.Message):
    """See https://docs.temporal.io/docs/concepts/task-queues/"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    NORMAL_NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    kind: temporalio.api.enums.v1.task_queue_pb2.TaskQueueKind.ValueType
    """Default: TASK_QUEUE_KIND_NORMAL."""
    normal_name: builtins.str
    """Iff kind == TASK_QUEUE_KIND_STICKY, then this field contains the name of
    the normal task queue that the sticky worker is running on.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        kind: temporalio.api.enums.v1.task_queue_pb2.TaskQueueKind.ValueType = ...,
        normal_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "kind", b"kind", "name", b"name", "normal_name", b"normal_name"
        ],
    ) -> None: ...

global___TaskQueue = TaskQueue

class TaskQueueMetadata(google.protobuf.message.Message):
    """Only applies to activity task queues"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_TASKS_PER_SECOND_FIELD_NUMBER: builtins.int
    @property
    def max_tasks_per_second(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """Allows throttling dispatch of tasks from this queue"""
    def __init__(
        self,
        *,
        max_tasks_per_second: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "max_tasks_per_second", b"max_tasks_per_second"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "max_tasks_per_second", b"max_tasks_per_second"
        ],
    ) -> None: ...

global___TaskQueueMetadata = TaskQueueMetadata

class TaskQueueStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKLOG_COUNT_HINT_FIELD_NUMBER: builtins.int
    READ_LEVEL_FIELD_NUMBER: builtins.int
    ACK_LEVEL_FIELD_NUMBER: builtins.int
    RATE_PER_SECOND_FIELD_NUMBER: builtins.int
    TASK_ID_BLOCK_FIELD_NUMBER: builtins.int
    backlog_count_hint: builtins.int
    read_level: builtins.int
    ack_level: builtins.int
    rate_per_second: builtins.float
    @property
    def task_id_block(self) -> global___TaskIdBlock: ...
    def __init__(
        self,
        *,
        backlog_count_hint: builtins.int = ...,
        read_level: builtins.int = ...,
        ack_level: builtins.int = ...,
        rate_per_second: builtins.float = ...,
        task_id_block: global___TaskIdBlock | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["task_id_block", b"task_id_block"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ack_level",
            b"ack_level",
            "backlog_count_hint",
            b"backlog_count_hint",
            "rate_per_second",
            b"rate_per_second",
            "read_level",
            b"read_level",
            "task_id_block",
            b"task_id_block",
        ],
    ) -> None: ...

global___TaskQueueStatus = TaskQueueStatus

class TaskIdBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_ID_FIELD_NUMBER: builtins.int
    END_ID_FIELD_NUMBER: builtins.int
    start_id: builtins.int
    end_id: builtins.int
    def __init__(
        self,
        *,
        start_id: builtins.int = ...,
        end_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "end_id", b"end_id", "start_id", b"start_id"
        ],
    ) -> None: ...

global___TaskIdBlock = TaskIdBlock

class TaskQueuePartitionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    OWNER_HOST_NAME_FIELD_NUMBER: builtins.int
    key: builtins.str
    owner_host_name: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        owner_host_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "key", b"key", "owner_host_name", b"owner_host_name"
        ],
    ) -> None: ...

global___TaskQueuePartitionMetadata = TaskQueuePartitionMetadata

class PollerInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_ACCESS_TIME_FIELD_NUMBER: builtins.int
    IDENTITY_FIELD_NUMBER: builtins.int
    RATE_PER_SECOND_FIELD_NUMBER: builtins.int
    WORKER_VERSION_CAPABILITIES_FIELD_NUMBER: builtins.int
    @property
    def last_access_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    identity: builtins.str
    rate_per_second: builtins.float
    @property
    def worker_version_capabilities(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkerVersionCapabilities:
        """If a worker has opted into the worker versioning feature while polling, its capabilities will
        appear here.
        """
    def __init__(
        self,
        *,
        last_access_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        identity: builtins.str = ...,
        rate_per_second: builtins.float = ...,
        worker_version_capabilities: temporalio.api.common.v1.message_pb2.WorkerVersionCapabilities
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "last_access_time",
            b"last_access_time",
            "worker_version_capabilities",
            b"worker_version_capabilities",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "identity",
            b"identity",
            "last_access_time",
            b"last_access_time",
            "rate_per_second",
            b"rate_per_second",
            "worker_version_capabilities",
            b"worker_version_capabilities",
        ],
    ) -> None: ...

global___PollerInfo = PollerInfo

class StickyExecutionAttributes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKER_TASK_QUEUE_FIELD_NUMBER: builtins.int
    SCHEDULE_TO_START_TIMEOUT_FIELD_NUMBER: builtins.int
    @property
    def worker_task_queue(self) -> global___TaskQueue: ...
    @property
    def schedule_to_start_timeout(self) -> google.protobuf.duration_pb2.Duration:
        """(-- api-linter: core::0140::prepositions=disabled
        aip.dev/not-precedent: "to" is used to indicate interval. --)
        """
    def __init__(
        self,
        *,
        worker_task_queue: global___TaskQueue | None = ...,
        schedule_to_start_timeout: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "schedule_to_start_timeout",
            b"schedule_to_start_timeout",
            "worker_task_queue",
            b"worker_task_queue",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "schedule_to_start_timeout",
            b"schedule_to_start_timeout",
            "worker_task_queue",
            b"worker_task_queue",
        ],
    ) -> None: ...

global___StickyExecutionAttributes = StickyExecutionAttributes

class CompatibleVersionSet(google.protobuf.message.Message):
    """Used by the worker versioning APIs, represents an unordered set of one or more versions which are
    considered to be compatible with each other. Currently the versions are always worker build IDs.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_IDS_FIELD_NUMBER: builtins.int
    @property
    def build_ids(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """All the compatible versions, unordered, except for the last element, which is considered the set "default"."""
    def __init__(
        self,
        *,
        build_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["build_ids", b"build_ids"]
    ) -> None: ...

global___CompatibleVersionSet = CompatibleVersionSet

class TaskQueueReachability(google.protobuf.message.Message):
    """Reachability of tasks for a worker on a single task queue."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_QUEUE_FIELD_NUMBER: builtins.int
    REACHABILITY_FIELD_NUMBER: builtins.int
    task_queue: builtins.str
    @property
    def reachability(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        temporalio.api.enums.v1.task_queue_pb2.TaskReachability.ValueType
    ]:
        """Task reachability for a worker in a single task queue.
        See the TaskReachability docstring for information about each enum variant.
        If reachability is empty, this worker is considered unreachable in this task queue.
        """
    def __init__(
        self,
        *,
        task_queue: builtins.str = ...,
        reachability: collections.abc.Iterable[
            temporalio.api.enums.v1.task_queue_pb2.TaskReachability.ValueType
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "reachability", b"reachability", "task_queue", b"task_queue"
        ],
    ) -> None: ...

global___TaskQueueReachability = TaskQueueReachability

class BuildIdReachability(google.protobuf.message.Message):
    """Reachability of tasks for a worker by build id, in one or more task queues."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    TASK_QUEUE_REACHABILITY_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """A build id or empty if unversioned."""
    @property
    def task_queue_reachability(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___TaskQueueReachability
    ]:
        """Reachability per task queue."""
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
        task_queue_reachability: collections.abc.Iterable[
            global___TaskQueueReachability
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "build_id",
            b"build_id",
            "task_queue_reachability",
            b"task_queue_reachability",
        ],
    ) -> None: ...

global___BuildIdReachability = BuildIdReachability

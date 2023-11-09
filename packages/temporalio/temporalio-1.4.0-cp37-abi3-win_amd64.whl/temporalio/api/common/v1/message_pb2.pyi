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
import sys
import temporalio.api.enums.v1.common_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataBlob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENCODING_TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    encoding_type: temporalio.api.enums.v1.common_pb2.EncodingType.ValueType
    data: builtins.bytes
    def __init__(
        self,
        *,
        encoding_type: temporalio.api.enums.v1.common_pb2.EncodingType.ValueType = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "data", b"data", "encoding_type", b"encoding_type"
        ],
    ) -> None: ...

global___DataBlob = DataBlob

class Payloads(google.protobuf.message.Message):
    """See `Payload`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAYLOADS_FIELD_NUMBER: builtins.int
    @property
    def payloads(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Payload
    ]: ...
    def __init__(
        self,
        *,
        payloads: collections.abc.Iterable[global___Payload] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["payloads", b"payloads"]
    ) -> None: ...

global___Payloads = Payloads

class Payload(google.protobuf.message.Message):
    """Represents some binary (byte array) data (ex: activity input parameters or workflow result) with
    metadata which describes this binary data (format, encoding, encryption, etc). Serialization
    of the data may be user-defined.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    METADATA_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def metadata(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, builtins.bytes
    ]: ...
    data: builtins.bytes
    def __init__(
        self,
        *,
        metadata: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["data", b"data", "metadata", b"metadata"],
    ) -> None: ...

global___Payload = Payload

class SearchAttributes(google.protobuf.message.Message):
    """A user-defined set of *indexed* fields that are used/exposed when listing/searching workflows.
    The payload is not serialized in a user-defined way.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class IndexedFieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Payload: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Payload | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    INDEXED_FIELDS_FIELD_NUMBER: builtins.int
    @property
    def indexed_fields(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___Payload
    ]: ...
    def __init__(
        self,
        *,
        indexed_fields: collections.abc.Mapping[builtins.str, global___Payload]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["indexed_fields", b"indexed_fields"]
    ) -> None: ...

global___SearchAttributes = SearchAttributes

class Memo(google.protobuf.message.Message):
    """A user-defined set of *unindexed* fields that are exposed when listing/searching workflows"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Payload: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Payload | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___Payload
    ]: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Mapping[builtins.str, global___Payload] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["fields", b"fields"]
    ) -> None: ...

global___Memo = Memo

class Header(google.protobuf.message.Message):
    """Contains metadata that can be attached to a variety of requests, like starting a workflow, and
    can be propagated between, for example, workflows and activities.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Payload: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Payload | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___Payload
    ]: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Mapping[builtins.str, global___Payload] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["fields", b"fields"]
    ) -> None: ...

global___Header = Header

class WorkflowExecution(google.protobuf.message.Message):
    """Identifies a specific workflow within a namespace. Practically speaking, because run_id is a
    uuid, a workflow execution is globally unique. Note that many commands allow specifying an empty
    run id as a way of saying "target the latest run of the workflow".
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKFLOW_ID_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    workflow_id: builtins.str
    run_id: builtins.str
    def __init__(
        self,
        *,
        workflow_id: builtins.str = ...,
        run_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "run_id", b"run_id", "workflow_id", b"workflow_id"
        ],
    ) -> None: ...

global___WorkflowExecution = WorkflowExecution

class WorkflowType(google.protobuf.message.Message):
    """Represents the identifier used by a workflow author to define the workflow. Typically, the
    name of a function. This is sometimes referred to as the workflow's "name"
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___WorkflowType = WorkflowType

class ActivityType(google.protobuf.message.Message):
    """Represents the identifier used by a activity author to define the activity. Typically, the
    name of a function. This is sometimes referred to as the activity's "name"
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___ActivityType = ActivityType

class RetryPolicy(google.protobuf.message.Message):
    """How retries ought to be handled, usable by both workflows and activities"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INITIAL_INTERVAL_FIELD_NUMBER: builtins.int
    BACKOFF_COEFFICIENT_FIELD_NUMBER: builtins.int
    MAXIMUM_INTERVAL_FIELD_NUMBER: builtins.int
    MAXIMUM_ATTEMPTS_FIELD_NUMBER: builtins.int
    NON_RETRYABLE_ERROR_TYPES_FIELD_NUMBER: builtins.int
    @property
    def initial_interval(self) -> google.protobuf.duration_pb2.Duration:
        """Interval of the first retry. If retryBackoffCoefficient is 1.0 then it is used for all retries."""
    backoff_coefficient: builtins.float
    """Coefficient used to calculate the next retry interval.
    The next retry interval is previous interval multiplied by the coefficient.
    Must be 1 or larger.
    """
    @property
    def maximum_interval(self) -> google.protobuf.duration_pb2.Duration:
        """Maximum interval between retries. Exponential backoff leads to interval increase.
        This value is the cap of the increase. Default is 100x of the initial interval.
        """
    maximum_attempts: builtins.int
    """Maximum number of attempts. When exceeded the retries stop even if not expired yet.
    1 disables retries. 0 means unlimited (up to the timeouts)
    """
    @property
    def non_retryable_error_types(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Non-Retryable errors types. Will stop retrying if the error type matches this list. Note that
        this is not a substring match, the error *type* (not message) must match exactly.
        """
    def __init__(
        self,
        *,
        initial_interval: google.protobuf.duration_pb2.Duration | None = ...,
        backoff_coefficient: builtins.float = ...,
        maximum_interval: google.protobuf.duration_pb2.Duration | None = ...,
        maximum_attempts: builtins.int = ...,
        non_retryable_error_types: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "initial_interval",
            b"initial_interval",
            "maximum_interval",
            b"maximum_interval",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "backoff_coefficient",
            b"backoff_coefficient",
            "initial_interval",
            b"initial_interval",
            "maximum_attempts",
            b"maximum_attempts",
            "maximum_interval",
            b"maximum_interval",
            "non_retryable_error_types",
            b"non_retryable_error_types",
        ],
    ) -> None: ...

global___RetryPolicy = RetryPolicy

class MeteringMetadata(google.protobuf.message.Message):
    """Metadata relevant for metering purposes"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NONFIRST_LOCAL_ACTIVITY_EXECUTION_ATTEMPTS_FIELD_NUMBER: builtins.int
    nonfirst_local_activity_execution_attempts: builtins.int
    """Count of local activities which have begun an execution attempt during this workflow task,
    and whose first attempt occurred in some previous task. This is used for metering
    purposes, and does not affect workflow state.

    (-- api-linter: core::0141::forbidden-types=disabled
        aip.dev/not-precedent: Negative values make no sense to represent. --)
    """
    def __init__(
        self,
        *,
        nonfirst_local_activity_execution_attempts: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "nonfirst_local_activity_execution_attempts",
            b"nonfirst_local_activity_execution_attempts",
        ],
    ) -> None: ...

global___MeteringMetadata = MeteringMetadata

class WorkerVersionStamp(google.protobuf.message.Message):
    """Identifies the version(s) of a worker that processed a task"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    BUNDLE_ID_FIELD_NUMBER: builtins.int
    USE_VERSIONING_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """An opaque whole-worker identifier. Replaces the deprecated `binary_checksum` field when this
    message is included in requests which previously used that.
    """
    bundle_id: builtins.str
    """Set if the worker used a dynamically loadable bundle to process
    the task. The bundle could be a WASM blob, JS bundle, etc.
    """
    use_versioning: builtins.bool
    """If set, the worker is opting in to worker versioning. Otherwise, this is used only as a
    marker for workflow reset points and the BuildIDs search attribute.
    """
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
        bundle_id: builtins.str = ...,
        use_versioning: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "build_id",
            b"build_id",
            "bundle_id",
            b"bundle_id",
            "use_versioning",
            b"use_versioning",
        ],
    ) -> None: ...

global___WorkerVersionStamp = WorkerVersionStamp

class WorkerVersionCapabilities(google.protobuf.message.Message):
    """Identifies the version(s) that a worker is compatible with when polling or identifying itself,
    and whether or not this worker is opting into the build-id based versioning feature. This is
    used by matching to determine which workers ought to receive what tasks.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUILD_ID_FIELD_NUMBER: builtins.int
    USE_VERSIONING_FIELD_NUMBER: builtins.int
    build_id: builtins.str
    """An opaque whole-worker identifier"""
    use_versioning: builtins.bool
    """If set, the worker is opting in to worker versioning, and wishes to only receive appropriate
    tasks.
    """
    def __init__(
        self,
        *,
        build_id: builtins.str = ...,
        use_versioning: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "build_id", b"build_id", "use_versioning", b"use_versioning"
        ],
    ) -> None: ...

global___WorkerVersionCapabilities = WorkerVersionCapabilities

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import temporalio.api.common.v1.message_pb2
import temporalio.api.failure.v1.message_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ParentClosePolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ParentClosePolicyEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ParentClosePolicy.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PARENT_CLOSE_POLICY_UNSPECIFIED: _ParentClosePolicy.ValueType  # 0
    """Let's the server set the default."""
    PARENT_CLOSE_POLICY_TERMINATE: _ParentClosePolicy.ValueType  # 1
    """Terminate means terminating the child workflow."""
    PARENT_CLOSE_POLICY_ABANDON: _ParentClosePolicy.ValueType  # 2
    """Abandon means not doing anything on the child workflow."""
    PARENT_CLOSE_POLICY_REQUEST_CANCEL: _ParentClosePolicy.ValueType  # 3
    """Cancel means requesting cancellation on the child workflow."""

class ParentClosePolicy(
    _ParentClosePolicy, metaclass=_ParentClosePolicyEnumTypeWrapper
):
    """Used by the service to determine the fate of a child workflow
    in case its parent is closed.
    """

PARENT_CLOSE_POLICY_UNSPECIFIED: ParentClosePolicy.ValueType  # 0
"""Let's the server set the default."""
PARENT_CLOSE_POLICY_TERMINATE: ParentClosePolicy.ValueType  # 1
"""Terminate means terminating the child workflow."""
PARENT_CLOSE_POLICY_ABANDON: ParentClosePolicy.ValueType  # 2
"""Abandon means not doing anything on the child workflow."""
PARENT_CLOSE_POLICY_REQUEST_CANCEL: ParentClosePolicy.ValueType  # 3
"""Cancel means requesting cancellation on the child workflow."""
global___ParentClosePolicy = ParentClosePolicy

class _StartChildWorkflowExecutionFailedCause:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StartChildWorkflowExecutionFailedCauseEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _StartChildWorkflowExecutionFailedCause.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED: _StartChildWorkflowExecutionFailedCause.ValueType  # 0
    START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_EXISTS: _StartChildWorkflowExecutionFailedCause.ValueType  # 1

class StartChildWorkflowExecutionFailedCause(
    _StartChildWorkflowExecutionFailedCause,
    metaclass=_StartChildWorkflowExecutionFailedCauseEnumTypeWrapper,
):
    """Possible causes of failure to start a child workflow"""

START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED: StartChildWorkflowExecutionFailedCause.ValueType  # 0
START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_EXISTS: StartChildWorkflowExecutionFailedCause.ValueType  # 1
global___StartChildWorkflowExecutionFailedCause = StartChildWorkflowExecutionFailedCause

class _ChildWorkflowCancellationType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ChildWorkflowCancellationTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ChildWorkflowCancellationType.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ABANDON: _ChildWorkflowCancellationType.ValueType  # 0
    """Do not request cancellation of the child workflow if already scheduled"""
    TRY_CANCEL: _ChildWorkflowCancellationType.ValueType  # 1
    """Initiate a cancellation request and immediately report cancellation to the parent."""
    WAIT_CANCELLATION_COMPLETED: _ChildWorkflowCancellationType.ValueType  # 2
    """Wait for child cancellation completion."""
    WAIT_CANCELLATION_REQUESTED: _ChildWorkflowCancellationType.ValueType  # 3
    """Request cancellation of the child and wait for confirmation that the request was received."""

class ChildWorkflowCancellationType(
    _ChildWorkflowCancellationType,
    metaclass=_ChildWorkflowCancellationTypeEnumTypeWrapper,
):
    """Controls at which point to report back to lang when a child workflow is cancelled"""

ABANDON: ChildWorkflowCancellationType.ValueType  # 0
"""Do not request cancellation of the child workflow if already scheduled"""
TRY_CANCEL: ChildWorkflowCancellationType.ValueType  # 1
"""Initiate a cancellation request and immediately report cancellation to the parent."""
WAIT_CANCELLATION_COMPLETED: ChildWorkflowCancellationType.ValueType  # 2
"""Wait for child cancellation completion."""
WAIT_CANCELLATION_REQUESTED: ChildWorkflowCancellationType.ValueType  # 3
"""Request cancellation of the child and wait for confirmation that the request was received."""
global___ChildWorkflowCancellationType = ChildWorkflowCancellationType

class ChildWorkflowResult(google.protobuf.message.Message):
    """Used by core to resolve child workflow executions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPLETED_FIELD_NUMBER: builtins.int
    FAILED_FIELD_NUMBER: builtins.int
    CANCELLED_FIELD_NUMBER: builtins.int
    @property
    def completed(self) -> global___Success: ...
    @property
    def failed(self) -> global___Failure: ...
    @property
    def cancelled(self) -> global___Cancellation: ...
    def __init__(
        self,
        *,
        completed: global___Success | None = ...,
        failed: global___Failure | None = ...,
        cancelled: global___Cancellation | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "cancelled",
            b"cancelled",
            "completed",
            b"completed",
            "failed",
            b"failed",
            "status",
            b"status",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cancelled",
            b"cancelled",
            "completed",
            b"completed",
            "failed",
            b"failed",
            "status",
            b"status",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["status", b"status"]
    ) -> typing_extensions.Literal["completed", "failed", "cancelled"] | None: ...

global___ChildWorkflowResult = ChildWorkflowResult

class Success(google.protobuf.message.Message):
    """Used in ChildWorkflowResult to report successful completion."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> temporalio.api.common.v1.message_pb2.Payload: ...
    def __init__(
        self,
        *,
        result: temporalio.api.common.v1.message_pb2.Payload | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> None: ...

global___Success = Success

class Failure(google.protobuf.message.Message):
    """Used in ChildWorkflowResult to report non successful outcomes such as
    application failures, timeouts, terminations, and cancellations.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> None: ...

global___Failure = Failure

class Cancellation(google.protobuf.message.Message):
    """Used in ChildWorkflowResult to report cancellation.
    Failure should be ChildWorkflowFailure with a CanceledFailure cause.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> None: ...

global___Cancellation = Cancellation

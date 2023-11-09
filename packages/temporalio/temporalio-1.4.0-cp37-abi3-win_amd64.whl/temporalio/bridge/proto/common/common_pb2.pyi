"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _VersioningIntent:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VersioningIntentEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _VersioningIntent.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _VersioningIntent.ValueType  # 0
    """Indicates that core should choose the most sensible default behavior for the type of
    command, accounting for whether the command will be run on the same task queue as the current
    worker.
    """
    COMPATIBLE: _VersioningIntent.ValueType  # 1
    """Indicates that the command should run on a worker with compatible version if possible. It may
    not be possible if the target task queue does not also have knowledge of the current worker's
    build ID.
    """
    DEFAULT: _VersioningIntent.ValueType  # 2
    """Indicates that the command should run on the target task queue's current overall-default
    build ID.
    """

class VersioningIntent(_VersioningIntent, metaclass=_VersioningIntentEnumTypeWrapper):
    """An indication of user's intent concerning what Build ID versioning approach should be used for
    a specific command
    """

UNSPECIFIED: VersioningIntent.ValueType  # 0
"""Indicates that core should choose the most sensible default behavior for the type of
command, accounting for whether the command will be run on the same task queue as the current
worker.
"""
COMPATIBLE: VersioningIntent.ValueType  # 1
"""Indicates that the command should run on a worker with compatible version if possible. It may
not be possible if the target task queue does not also have knowledge of the current worker's
build ID.
"""
DEFAULT: VersioningIntent.ValueType  # 2
"""Indicates that the command should run on the target task queue's current overall-default
build ID.
"""
global___VersioningIntent = VersioningIntent

class NamespacedWorkflowExecution(google.protobuf.message.Message):
    """Identifying information about a particular workflow execution, including namespace"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    WORKFLOW_ID_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    """Namespace the workflow run is located in"""
    workflow_id: builtins.str
    """Can never be empty"""
    run_id: builtins.str
    """May be empty if the most recent run of the workflow with the given ID is being targeted"""
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
        workflow_id: builtins.str = ...,
        run_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "namespace",
            b"namespace",
            "run_id",
            b"run_id",
            "workflow_id",
            b"workflow_id",
        ],
    ) -> None: ...

global___NamespacedWorkflowExecution = NamespacedWorkflowExecution

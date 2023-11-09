"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
We have to alter this to prevent gRPC health clash"""
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

class HealthCheckRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_FIELD_NUMBER: builtins.int
    service: builtins.str
    def __init__(
        self,
        *,
        service: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["service", b"service"]
    ) -> None: ...

global___HealthCheckRequest = HealthCheckRequest

class HealthCheckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ServingStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ServingStatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            HealthCheckResponse._ServingStatus.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: HealthCheckResponse._ServingStatus.ValueType  # 0
        SERVING: HealthCheckResponse._ServingStatus.ValueType  # 1
        NOT_SERVING: HealthCheckResponse._ServingStatus.ValueType  # 2
        SERVICE_UNKNOWN: HealthCheckResponse._ServingStatus.ValueType  # 3
        """Used only by the Watch method."""

    class ServingStatus(_ServingStatus, metaclass=_ServingStatusEnumTypeWrapper): ...
    UNKNOWN: HealthCheckResponse.ServingStatus.ValueType  # 0
    SERVING: HealthCheckResponse.ServingStatus.ValueType  # 1
    NOT_SERVING: HealthCheckResponse.ServingStatus.ValueType  # 2
    SERVICE_UNKNOWN: HealthCheckResponse.ServingStatus.ValueType  # 3
    """Used only by the Watch method."""

    STATUS_FIELD_NUMBER: builtins.int
    status: global___HealthCheckResponse.ServingStatus.ValueType
    def __init__(
        self,
        *,
        status: global___HealthCheckResponse.ServingStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["status", b"status"]
    ) -> None: ...

global___HealthCheckResponse = HealthCheckResponse

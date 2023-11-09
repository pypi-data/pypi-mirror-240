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
import google.protobuf.descriptor
import google.protobuf.message
import sys
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.interaction_type_pb2
import temporalio.api.failure.v1.message_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Meta(google.protobuf.message.Message):
    """Meta carries metadata about an interaction for use by the system (i.e. not
    generall user-visible)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    EVENT_ID_FIELD_NUMBER: builtins.int
    INTERACTION_TYPE_FIELD_NUMBER: builtins.int
    IDENTITY_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """An ID with workflow-scoped uniqueness for this interaction"""
    event_id: builtins.int
    """The event ID after which this interaction can execute. The effects of
    history up to and including this event ID should be visible to the
    interaction when it executes.
    """
    interaction_type: temporalio.api.enums.v1.interaction_type_pb2.InteractionType.ValueType
    """The type of this interaction."""
    identity: builtins.str
    """A string identifying the agent that requested this interaction."""
    request_id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        event_id: builtins.int = ...,
        interaction_type: temporalio.api.enums.v1.interaction_type_pb2.InteractionType.ValueType = ...,
        identity: builtins.str = ...,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "event_id",
            b"event_id",
            "id",
            b"id",
            "identity",
            b"identity",
            "interaction_type",
            b"interaction_type",
            "request_id",
            b"request_id",
        ],
    ) -> None: ...

global___Meta = Meta

class Input(google.protobuf.message.Message):
    """Input carries interaction input that comes from the caller."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> temporalio.api.common.v1.message_pb2.Header:
        """Headers that are passed with the interaction to and from the processing workflow.
        These can include things like auth or tracing tokens.
        """
    name: builtins.str
    """The name of the input handler to invoke on the target workflow"""
    @property
    def args(self) -> temporalio.api.common.v1.message_pb2.Payloads:
        """The arguments to pass to the named handler."""
    def __init__(
        self,
        *,
        header: temporalio.api.common.v1.message_pb2.Header | None = ...,
        name: builtins.str = ...,
        args: temporalio.api.common.v1.message_pb2.Payloads | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["args", b"args", "header", b"header"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "args", b"args", "header", b"header", "name", b"name"
        ],
    ) -> None: ...

global___Input = Input

class Output(google.protobuf.message.Message):
    """Output carries the output data from an interaction."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> temporalio.api.common.v1.message_pb2.Header:
        """Headers that are passed with the interaction to and from the processing workflow.
        These can include things like auth or tracing tokens.
        """
    @property
    def success(self) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        header: temporalio.api.common.v1.message_pb2.Header | None = ...,
        success: temporalio.api.common.v1.message_pb2.Payloads | None = ...,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "failure",
            b"failure",
            "header",
            b"header",
            "result",
            b"result",
            "success",
            b"success",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "failure",
            b"failure",
            "header",
            b"header",
            "result",
            b"result",
            "success",
            b"success",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["result", b"result"]
    ) -> typing_extensions.Literal["success", "failure"] | None: ...

global___Output = Output

class Invocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> global___Meta: ...
    @property
    def input(self) -> global___Input: ...
    def __init__(
        self,
        *,
        meta: global___Meta | None = ...,
        input: global___Input | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input", "meta", b"meta"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["input", b"input", "meta", b"meta"]
    ) -> None: ...

global___Invocation = Invocation

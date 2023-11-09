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
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NamespaceState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NamespaceStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _NamespaceState.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NAMESPACE_STATE_UNSPECIFIED: _NamespaceState.ValueType  # 0
    NAMESPACE_STATE_REGISTERED: _NamespaceState.ValueType  # 1
    NAMESPACE_STATE_DEPRECATED: _NamespaceState.ValueType  # 2
    NAMESPACE_STATE_DELETED: _NamespaceState.ValueType  # 3

class NamespaceState(_NamespaceState, metaclass=_NamespaceStateEnumTypeWrapper): ...

NAMESPACE_STATE_UNSPECIFIED: NamespaceState.ValueType  # 0
NAMESPACE_STATE_REGISTERED: NamespaceState.ValueType  # 1
NAMESPACE_STATE_DEPRECATED: NamespaceState.ValueType  # 2
NAMESPACE_STATE_DELETED: NamespaceState.ValueType  # 3
global___NamespaceState = NamespaceState

class _ArchivalState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ArchivalStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ArchivalState.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ARCHIVAL_STATE_UNSPECIFIED: _ArchivalState.ValueType  # 0
    ARCHIVAL_STATE_DISABLED: _ArchivalState.ValueType  # 1
    ARCHIVAL_STATE_ENABLED: _ArchivalState.ValueType  # 2

class ArchivalState(_ArchivalState, metaclass=_ArchivalStateEnumTypeWrapper): ...

ARCHIVAL_STATE_UNSPECIFIED: ArchivalState.ValueType  # 0
ARCHIVAL_STATE_DISABLED: ArchivalState.ValueType  # 1
ARCHIVAL_STATE_ENABLED: ArchivalState.ValueType  # 2
global___ArchivalState = ArchivalState

class _ReplicationState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReplicationStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ReplicationState.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    REPLICATION_STATE_UNSPECIFIED: _ReplicationState.ValueType  # 0
    REPLICATION_STATE_NORMAL: _ReplicationState.ValueType  # 1
    REPLICATION_STATE_HANDOVER: _ReplicationState.ValueType  # 2

class ReplicationState(
    _ReplicationState, metaclass=_ReplicationStateEnumTypeWrapper
): ...

REPLICATION_STATE_UNSPECIFIED: ReplicationState.ValueType  # 0
REPLICATION_STATE_NORMAL: ReplicationState.ValueType  # 1
REPLICATION_STATE_HANDOVER: ReplicationState.ValueType  # 2
global___ReplicationState = ReplicationState

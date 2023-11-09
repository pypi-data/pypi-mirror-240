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

class _EncodingType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EncodingTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _EncodingType.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ENCODING_TYPE_UNSPECIFIED: _EncodingType.ValueType  # 0
    ENCODING_TYPE_PROTO3: _EncodingType.ValueType  # 1
    ENCODING_TYPE_JSON: _EncodingType.ValueType  # 2

class EncodingType(_EncodingType, metaclass=_EncodingTypeEnumTypeWrapper): ...

ENCODING_TYPE_UNSPECIFIED: EncodingType.ValueType  # 0
ENCODING_TYPE_PROTO3: EncodingType.ValueType  # 1
ENCODING_TYPE_JSON: EncodingType.ValueType  # 2
global___EncodingType = EncodingType

class _IndexedValueType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IndexedValueTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _IndexedValueType.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INDEXED_VALUE_TYPE_UNSPECIFIED: _IndexedValueType.ValueType  # 0
    INDEXED_VALUE_TYPE_TEXT: _IndexedValueType.ValueType  # 1
    INDEXED_VALUE_TYPE_KEYWORD: _IndexedValueType.ValueType  # 2
    INDEXED_VALUE_TYPE_INT: _IndexedValueType.ValueType  # 3
    INDEXED_VALUE_TYPE_DOUBLE: _IndexedValueType.ValueType  # 4
    INDEXED_VALUE_TYPE_BOOL: _IndexedValueType.ValueType  # 5
    INDEXED_VALUE_TYPE_DATETIME: _IndexedValueType.ValueType  # 6
    INDEXED_VALUE_TYPE_KEYWORD_LIST: _IndexedValueType.ValueType  # 7

class IndexedValueType(
    _IndexedValueType, metaclass=_IndexedValueTypeEnumTypeWrapper
): ...

INDEXED_VALUE_TYPE_UNSPECIFIED: IndexedValueType.ValueType  # 0
INDEXED_VALUE_TYPE_TEXT: IndexedValueType.ValueType  # 1
INDEXED_VALUE_TYPE_KEYWORD: IndexedValueType.ValueType  # 2
INDEXED_VALUE_TYPE_INT: IndexedValueType.ValueType  # 3
INDEXED_VALUE_TYPE_DOUBLE: IndexedValueType.ValueType  # 4
INDEXED_VALUE_TYPE_BOOL: IndexedValueType.ValueType  # 5
INDEXED_VALUE_TYPE_DATETIME: IndexedValueType.ValueType  # 6
INDEXED_VALUE_TYPE_KEYWORD_LIST: IndexedValueType.ValueType  # 7
global___IndexedValueType = IndexedValueType

class _Severity:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SeverityEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Severity.ValueType],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SEVERITY_UNSPECIFIED: _Severity.ValueType  # 0
    SEVERITY_HIGH: _Severity.ValueType  # 1
    SEVERITY_MEDIUM: _Severity.ValueType  # 2
    SEVERITY_LOW: _Severity.ValueType  # 3

class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper): ...

SEVERITY_UNSPECIFIED: Severity.ValueType  # 0
SEVERITY_HIGH: Severity.ValueType  # 1
SEVERITY_MEDIUM: Severity.ValueType  # 2
SEVERITY_LOW: Severity.ValueType  # 3
global___Severity = Severity

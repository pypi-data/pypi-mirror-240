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
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import temporalio.api.enums.v1.common_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AddSearchAttributesRequest(google.protobuf.message.Message):
    """(-- Search Attribute --)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class SearchAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    @property
    def search_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between search attribute name and its IndexedValueType."""
    namespace: builtins.str
    def __init__(
        self,
        *,
        search_attributes: collections.abc.Mapping[
            builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        ]
        | None = ...,
        namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "namespace", b"namespace", "search_attributes", b"search_attributes"
        ],
    ) -> None: ...

global___AddSearchAttributesRequest = AddSearchAttributesRequest

class AddSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AddSearchAttributesResponse = AddSearchAttributesResponse

class RemoveSearchAttributesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEARCH_ATTRIBUTES_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    @property
    def search_attributes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Search attribute names to delete."""
    namespace: builtins.str
    def __init__(
        self,
        *,
        search_attributes: collections.abc.Iterable[builtins.str] | None = ...,
        namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "namespace", b"namespace", "search_attributes", b"search_attributes"
        ],
    ) -> None: ...

global___RemoveSearchAttributesRequest = RemoveSearchAttributesRequest

class RemoveSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RemoveSearchAttributesResponse = RemoveSearchAttributesResponse

class ListSearchAttributesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["namespace", b"namespace"]
    ) -> None: ...

global___ListSearchAttributesRequest = ListSearchAttributesRequest

class ListSearchAttributesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class CustomAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    class SystemAttributesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    class StorageSchemaEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    CUSTOM_ATTRIBUTES_FIELD_NUMBER: builtins.int
    SYSTEM_ATTRIBUTES_FIELD_NUMBER: builtins.int
    STORAGE_SCHEMA_FIELD_NUMBER: builtins.int
    @property
    def custom_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between custom (user-registered) search attribute name to its IndexedValueType."""
    @property
    def system_attributes(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
    ]:
        """Mapping between system (predefined) search attribute name to its IndexedValueType."""
    @property
    def storage_schema(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Mapping from the attribute name to the visibility storage native type."""
    def __init__(
        self,
        *,
        custom_attributes: collections.abc.Mapping[
            builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        ]
        | None = ...,
        system_attributes: collections.abc.Mapping[
            builtins.str, temporalio.api.enums.v1.common_pb2.IndexedValueType.ValueType
        ]
        | None = ...,
        storage_schema: collections.abc.Mapping[builtins.str, builtins.str]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "custom_attributes",
            b"custom_attributes",
            "storage_schema",
            b"storage_schema",
            "system_attributes",
            b"system_attributes",
        ],
    ) -> None: ...

global___ListSearchAttributesResponse = ListSearchAttributesResponse

class DeleteNamespaceRequest(google.protobuf.message.Message):
    """(-- api-linter: core::0135::request-unknown-fields=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
    (-- api-linter: core::0135::request-name-required=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["namespace", b"namespace"]
    ) -> None: ...

global___DeleteNamespaceRequest = DeleteNamespaceRequest

class DeleteNamespaceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELETED_NAMESPACE_FIELD_NUMBER: builtins.int
    deleted_namespace: builtins.str
    """Temporary namespace name that is used during reclaim resources step."""
    def __init__(
        self,
        *,
        deleted_namespace: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "deleted_namespace", b"deleted_namespace"
        ],
    ) -> None: ...

global___DeleteNamespaceResponse = DeleteNamespaceResponse

class AddOrUpdateRemoteClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRONTEND_ADDRESS_FIELD_NUMBER: builtins.int
    ENABLE_REMOTE_CLUSTER_CONNECTION_FIELD_NUMBER: builtins.int
    frontend_address: builtins.str
    """Frontend Address is a cross cluster accessible address."""
    enable_remote_cluster_connection: builtins.bool
    """Flag to enable / disable the cross cluster connection."""
    def __init__(
        self,
        *,
        frontend_address: builtins.str = ...,
        enable_remote_cluster_connection: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "enable_remote_cluster_connection",
            b"enable_remote_cluster_connection",
            "frontend_address",
            b"frontend_address",
        ],
    ) -> None: ...

global___AddOrUpdateRemoteClusterRequest = AddOrUpdateRemoteClusterRequest

class AddOrUpdateRemoteClusterResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AddOrUpdateRemoteClusterResponse = AddOrUpdateRemoteClusterResponse

class RemoveRemoteClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    cluster_name: builtins.str
    """Remote cluster name to be removed."""
    def __init__(
        self,
        *,
        cluster_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["cluster_name", b"cluster_name"]
    ) -> None: ...

global___RemoveRemoteClusterRequest = RemoveRemoteClusterRequest

class RemoveRemoteClusterResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RemoveRemoteClusterResponse = RemoveRemoteClusterResponse

class ListClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    next_page_token: builtins.bytes
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        next_page_token: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "next_page_token", b"next_page_token", "page_size", b"page_size"
        ],
    ) -> None: ...

global___ListClustersRequest = ListClustersRequest

class ListClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def clusters(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ClusterMetadata
    ]:
        """List of all cluster information"""
    next_page_token: builtins.bytes
    def __init__(
        self,
        *,
        clusters: collections.abc.Iterable[global___ClusterMetadata] | None = ...,
        next_page_token: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "clusters", b"clusters", "next_page_token", b"next_page_token"
        ],
    ) -> None: ...

global___ListClustersResponse = ListClustersResponse

class ClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    INITIAL_FAILOVER_VERSION_FIELD_NUMBER: builtins.int
    HISTORY_SHARD_COUNT_FIELD_NUMBER: builtins.int
    IS_CONNECTION_ENABLED_FIELD_NUMBER: builtins.int
    cluster_name: builtins.str
    """Name of the cluster name."""
    cluster_id: builtins.str
    """Id of the cluster."""
    address: builtins.str
    """Cluster accessible address."""
    initial_failover_version: builtins.int
    """A unique failover version across all connected clusters."""
    history_shard_count: builtins.int
    """History service shard number."""
    is_connection_enabled: builtins.bool
    """A flag to indicate if a connection is active."""
    def __init__(
        self,
        *,
        cluster_name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        address: builtins.str = ...,
        initial_failover_version: builtins.int = ...,
        history_shard_count: builtins.int = ...,
        is_connection_enabled: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "address",
            b"address",
            "cluster_id",
            b"cluster_id",
            "cluster_name",
            b"cluster_name",
            "history_shard_count",
            b"history_shard_count",
            "initial_failover_version",
            b"initial_failover_version",
            "is_connection_enabled",
            b"is_connection_enabled",
        ],
    ) -> None: ...

global___ClusterMetadata = ClusterMetadata

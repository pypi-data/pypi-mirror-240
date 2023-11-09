# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/operatorservice/v1/request_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.enums.v1 import (
    common_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_common__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n6temporal/api/operatorservice/v1/request_response.proto\x12\x1ftemporal.api.operatorservice.v1\x1a"temporal/api/enums/v1/common.proto"\xff\x01\n\x1a\x41\x64\x64SearchAttributesRequest\x12l\n\x11search_attributes\x18\x01 \x03(\x0b\x32Q.temporal.api.operatorservice.v1.AddSearchAttributesRequest.SearchAttributesEntry\x12\x11\n\tnamespace\x18\x02 \x01(\t\x1a`\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01"\x1d\n\x1b\x41\x64\x64SearchAttributesResponse"M\n\x1dRemoveSearchAttributesRequest\x12\x19\n\x11search_attributes\x18\x01 \x03(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t" \n\x1eRemoveSearchAttributesResponse"0\n\x1bListSearchAttributesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"\xe2\x04\n\x1cListSearchAttributesResponse\x12n\n\x11\x63ustom_attributes\x18\x01 \x03(\x0b\x32S.temporal.api.operatorservice.v1.ListSearchAttributesResponse.CustomAttributesEntry\x12n\n\x11system_attributes\x18\x02 \x03(\x0b\x32S.temporal.api.operatorservice.v1.ListSearchAttributesResponse.SystemAttributesEntry\x12h\n\x0estorage_schema\x18\x03 \x03(\x0b\x32P.temporal.api.operatorservice.v1.ListSearchAttributesResponse.StorageSchemaEntry\x1a`\n\x15\x43ustomAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01\x1a`\n\x15SystemAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0e\x32\'.temporal.api.enums.v1.IndexedValueType:\x02\x38\x01\x1a\x34\n\x12StorageSchemaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"+\n\x16\x44\x65leteNamespaceRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"4\n\x17\x44\x65leteNamespaceResponse\x12\x19\n\x11\x64\x65leted_namespace\x18\x01 \x01(\t"e\n\x1f\x41\x64\x64OrUpdateRemoteClusterRequest\x12\x18\n\x10\x66rontend_address\x18\x01 \x01(\t\x12(\n enable_remote_cluster_connection\x18\x02 \x01(\x08""\n AddOrUpdateRemoteClusterResponse"2\n\x1aRemoveRemoteClusterRequest\x12\x14\n\x0c\x63luster_name\x18\x01 \x01(\t"\x1d\n\x1bRemoveRemoteClusterResponse"A\n\x13ListClustersRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\x0c"s\n\x14ListClustersResponse\x12\x42\n\x08\x63lusters\x18\x01 \x03(\x0b\x32\x30.temporal.api.operatorservice.v1.ClusterMetadata\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\x0c"\xaa\x01\n\x0f\x43lusterMetadata\x12\x14\n\x0c\x63luster_name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12 \n\x18initial_failover_version\x18\x04 \x01(\x03\x12\x1b\n\x13history_shard_count\x18\x05 \x01(\x05\x12\x1d\n\x15is_connection_enabled\x18\x06 \x01(\x08\x42\xbe\x01\n"io.temporal.api.operatorservice.v1B\x14RequestResponseProtoP\x01Z5go.temporal.io/api/operatorservice/v1;operatorservice\xaa\x02!Temporalio.Api.OperatorService.V1\xea\x02$Temporalio::Api::OperatorService::V1b\x06proto3'
)


_ADDSEARCHATTRIBUTESREQUEST = DESCRIPTOR.message_types_by_name[
    "AddSearchAttributesRequest"
]
_ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY = (
    _ADDSEARCHATTRIBUTESREQUEST.nested_types_by_name["SearchAttributesEntry"]
)
_ADDSEARCHATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name[
    "AddSearchAttributesResponse"
]
_REMOVESEARCHATTRIBUTESREQUEST = DESCRIPTOR.message_types_by_name[
    "RemoveSearchAttributesRequest"
]
_REMOVESEARCHATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name[
    "RemoveSearchAttributesResponse"
]
_LISTSEARCHATTRIBUTESREQUEST = DESCRIPTOR.message_types_by_name[
    "ListSearchAttributesRequest"
]
_LISTSEARCHATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name[
    "ListSearchAttributesResponse"
]
_LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY = (
    _LISTSEARCHATTRIBUTESRESPONSE.nested_types_by_name["CustomAttributesEntry"]
)
_LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY = (
    _LISTSEARCHATTRIBUTESRESPONSE.nested_types_by_name["SystemAttributesEntry"]
)
_LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY = (
    _LISTSEARCHATTRIBUTESRESPONSE.nested_types_by_name["StorageSchemaEntry"]
)
_DELETENAMESPACEREQUEST = DESCRIPTOR.message_types_by_name["DeleteNamespaceRequest"]
_DELETENAMESPACERESPONSE = DESCRIPTOR.message_types_by_name["DeleteNamespaceResponse"]
_ADDORUPDATEREMOTECLUSTERREQUEST = DESCRIPTOR.message_types_by_name[
    "AddOrUpdateRemoteClusterRequest"
]
_ADDORUPDATEREMOTECLUSTERRESPONSE = DESCRIPTOR.message_types_by_name[
    "AddOrUpdateRemoteClusterResponse"
]
_REMOVEREMOTECLUSTERREQUEST = DESCRIPTOR.message_types_by_name[
    "RemoveRemoteClusterRequest"
]
_REMOVEREMOTECLUSTERRESPONSE = DESCRIPTOR.message_types_by_name[
    "RemoveRemoteClusterResponse"
]
_LISTCLUSTERSREQUEST = DESCRIPTOR.message_types_by_name["ListClustersRequest"]
_LISTCLUSTERSRESPONSE = DESCRIPTOR.message_types_by_name["ListClustersResponse"]
_CLUSTERMETADATA = DESCRIPTOR.message_types_by_name["ClusterMetadata"]
AddSearchAttributesRequest = _reflection.GeneratedProtocolMessageType(
    "AddSearchAttributesRequest",
    (_message.Message,),
    {
        "SearchAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "SearchAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY,
                "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.AddSearchAttributesRequest.SearchAttributesEntry)
            },
        ),
        "DESCRIPTOR": _ADDSEARCHATTRIBUTESREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.AddSearchAttributesRequest)
    },
)
_sym_db.RegisterMessage(AddSearchAttributesRequest)
_sym_db.RegisterMessage(AddSearchAttributesRequest.SearchAttributesEntry)

AddSearchAttributesResponse = _reflection.GeneratedProtocolMessageType(
    "AddSearchAttributesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDSEARCHATTRIBUTESRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.AddSearchAttributesResponse)
    },
)
_sym_db.RegisterMessage(AddSearchAttributesResponse)

RemoveSearchAttributesRequest = _reflection.GeneratedProtocolMessageType(
    "RemoveSearchAttributesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVESEARCHATTRIBUTESREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.RemoveSearchAttributesRequest)
    },
)
_sym_db.RegisterMessage(RemoveSearchAttributesRequest)

RemoveSearchAttributesResponse = _reflection.GeneratedProtocolMessageType(
    "RemoveSearchAttributesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVESEARCHATTRIBUTESRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.RemoveSearchAttributesResponse)
    },
)
_sym_db.RegisterMessage(RemoveSearchAttributesResponse)

ListSearchAttributesRequest = _reflection.GeneratedProtocolMessageType(
    "ListSearchAttributesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTSEARCHATTRIBUTESREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListSearchAttributesRequest)
    },
)
_sym_db.RegisterMessage(ListSearchAttributesRequest)

ListSearchAttributesResponse = _reflection.GeneratedProtocolMessageType(
    "ListSearchAttributesResponse",
    (_message.Message,),
    {
        "CustomAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "CustomAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY,
                "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListSearchAttributesResponse.CustomAttributesEntry)
            },
        ),
        "SystemAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "SystemAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY,
                "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListSearchAttributesResponse.SystemAttributesEntry)
            },
        ),
        "StorageSchemaEntry": _reflection.GeneratedProtocolMessageType(
            "StorageSchemaEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY,
                "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
                # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListSearchAttributesResponse.StorageSchemaEntry)
            },
        ),
        "DESCRIPTOR": _LISTSEARCHATTRIBUTESRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListSearchAttributesResponse)
    },
)
_sym_db.RegisterMessage(ListSearchAttributesResponse)
_sym_db.RegisterMessage(ListSearchAttributesResponse.CustomAttributesEntry)
_sym_db.RegisterMessage(ListSearchAttributesResponse.SystemAttributesEntry)
_sym_db.RegisterMessage(ListSearchAttributesResponse.StorageSchemaEntry)

DeleteNamespaceRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteNamespaceRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETENAMESPACEREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.DeleteNamespaceRequest)
    },
)
_sym_db.RegisterMessage(DeleteNamespaceRequest)

DeleteNamespaceResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteNamespaceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETENAMESPACERESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.DeleteNamespaceResponse)
    },
)
_sym_db.RegisterMessage(DeleteNamespaceResponse)

AddOrUpdateRemoteClusterRequest = _reflection.GeneratedProtocolMessageType(
    "AddOrUpdateRemoteClusterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDORUPDATEREMOTECLUSTERREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.AddOrUpdateRemoteClusterRequest)
    },
)
_sym_db.RegisterMessage(AddOrUpdateRemoteClusterRequest)

AddOrUpdateRemoteClusterResponse = _reflection.GeneratedProtocolMessageType(
    "AddOrUpdateRemoteClusterResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDORUPDATEREMOTECLUSTERRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.AddOrUpdateRemoteClusterResponse)
    },
)
_sym_db.RegisterMessage(AddOrUpdateRemoteClusterResponse)

RemoveRemoteClusterRequest = _reflection.GeneratedProtocolMessageType(
    "RemoveRemoteClusterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVEREMOTECLUSTERREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.RemoveRemoteClusterRequest)
    },
)
_sym_db.RegisterMessage(RemoveRemoteClusterRequest)

RemoveRemoteClusterResponse = _reflection.GeneratedProtocolMessageType(
    "RemoveRemoteClusterResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVEREMOTECLUSTERRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.RemoveRemoteClusterResponse)
    },
)
_sym_db.RegisterMessage(RemoveRemoteClusterResponse)

ListClustersRequest = _reflection.GeneratedProtocolMessageType(
    "ListClustersRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTCLUSTERSREQUEST,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListClustersRequest)
    },
)
_sym_db.RegisterMessage(ListClustersRequest)

ListClustersResponse = _reflection.GeneratedProtocolMessageType(
    "ListClustersResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTCLUSTERSRESPONSE,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ListClustersResponse)
    },
)
_sym_db.RegisterMessage(ListClustersResponse)

ClusterMetadata = _reflection.GeneratedProtocolMessageType(
    "ClusterMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLUSTERMETADATA,
        "__module__": "temporal.api.operatorservice.v1.request_response_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.operatorservice.v1.ClusterMetadata)
    },
)
_sym_db.RegisterMessage(ClusterMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n"io.temporal.api.operatorservice.v1B\024RequestResponseProtoP\001Z5go.temporal.io/api/operatorservice/v1;operatorservice\252\002!Temporalio.Api.OperatorService.V1\352\002$Temporalio::Api::OperatorService::V1'
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._options = None
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_options = b"8\001"
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._options = None
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_options = b"8\001"
    _ADDSEARCHATTRIBUTESREQUEST._serialized_start = 128
    _ADDSEARCHATTRIBUTESREQUEST._serialized_end = 383
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_start = 287
    _ADDSEARCHATTRIBUTESREQUEST_SEARCHATTRIBUTESENTRY._serialized_end = 383
    _ADDSEARCHATTRIBUTESRESPONSE._serialized_start = 385
    _ADDSEARCHATTRIBUTESRESPONSE._serialized_end = 414
    _REMOVESEARCHATTRIBUTESREQUEST._serialized_start = 416
    _REMOVESEARCHATTRIBUTESREQUEST._serialized_end = 493
    _REMOVESEARCHATTRIBUTESRESPONSE._serialized_start = 495
    _REMOVESEARCHATTRIBUTESRESPONSE._serialized_end = 527
    _LISTSEARCHATTRIBUTESREQUEST._serialized_start = 529
    _LISTSEARCHATTRIBUTESREQUEST._serialized_end = 577
    _LISTSEARCHATTRIBUTESRESPONSE._serialized_start = 580
    _LISTSEARCHATTRIBUTESRESPONSE._serialized_end = 1190
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_start = 942
    _LISTSEARCHATTRIBUTESRESPONSE_CUSTOMATTRIBUTESENTRY._serialized_end = 1038
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_start = 1040
    _LISTSEARCHATTRIBUTESRESPONSE_SYSTEMATTRIBUTESENTRY._serialized_end = 1136
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_start = 1138
    _LISTSEARCHATTRIBUTESRESPONSE_STORAGESCHEMAENTRY._serialized_end = 1190
    _DELETENAMESPACEREQUEST._serialized_start = 1192
    _DELETENAMESPACEREQUEST._serialized_end = 1235
    _DELETENAMESPACERESPONSE._serialized_start = 1237
    _DELETENAMESPACERESPONSE._serialized_end = 1289
    _ADDORUPDATEREMOTECLUSTERREQUEST._serialized_start = 1291
    _ADDORUPDATEREMOTECLUSTERREQUEST._serialized_end = 1392
    _ADDORUPDATEREMOTECLUSTERRESPONSE._serialized_start = 1394
    _ADDORUPDATEREMOTECLUSTERRESPONSE._serialized_end = 1428
    _REMOVEREMOTECLUSTERREQUEST._serialized_start = 1430
    _REMOVEREMOTECLUSTERREQUEST._serialized_end = 1480
    _REMOVEREMOTECLUSTERRESPONSE._serialized_start = 1482
    _REMOVEREMOTECLUSTERRESPONSE._serialized_end = 1511
    _LISTCLUSTERSREQUEST._serialized_start = 1513
    _LISTCLUSTERSREQUEST._serialized_end = 1578
    _LISTCLUSTERSRESPONSE._serialized_start = 1580
    _LISTCLUSTERSRESPONSE._serialized_end = 1695
    _CLUSTERMETADATA._serialized_start = 1698
    _CLUSTERMETADATA._serialized_end = 1868
# @@protoc_insertion_point(module_scope)

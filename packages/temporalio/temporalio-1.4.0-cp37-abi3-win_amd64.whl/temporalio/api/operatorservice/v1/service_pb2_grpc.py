# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from temporalio.api.operatorservice.v1 import (
    request_response_pb2 as temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2,
)


class OperatorServiceStub(object):
    """OperatorService API defines how Temporal SDKs and other clients interact with the Temporal server
    to perform administrative functions like registering a search attribute or a namespace.
    APIs in this file could be not compatible with Temporal Cloud, hence it's usage in SDKs should be limited by
    designated APIs that clearly state that they shouldn't be used by the main Application (Workflows & Activities) framework.
    (-- Search Attribute --)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSearchAttributes = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/AddSearchAttributes",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesResponse.FromString,
        )
        self.RemoveSearchAttributes = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/RemoveSearchAttributes",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesResponse.FromString,
        )
        self.ListSearchAttributes = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/ListSearchAttributes",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesResponse.FromString,
        )
        self.DeleteNamespace = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/DeleteNamespace",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceResponse.FromString,
        )
        self.AddOrUpdateRemoteCluster = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/AddOrUpdateRemoteCluster",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterResponse.FromString,
        )
        self.RemoveRemoteCluster = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/RemoveRemoteCluster",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterResponse.FromString,
        )
        self.ListClusters = channel.unary_unary(
            "/temporal.api.operatorservice.v1.OperatorService/ListClusters",
            request_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersRequest.SerializeToString,
            response_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersResponse.FromString,
        )


class OperatorServiceServicer(object):
    """OperatorService API defines how Temporal SDKs and other clients interact with the Temporal server
    to perform administrative functions like registering a search attribute or a namespace.
    APIs in this file could be not compatible with Temporal Cloud, hence it's usage in SDKs should be limited by
    designated APIs that clearly state that they shouldn't be used by the main Application (Workflows & Activities) framework.
    (-- Search Attribute --)
    """

    def AddSearchAttributes(self, request, context):
        """AddSearchAttributes add custom search attributes.

        Returns ALREADY_EXISTS status code if a Search Attribute with any of the specified names already exists
        Returns INTERNAL status code with temporal.api.errordetails.v1.SystemWorkflowFailure in Error Details if registration process fails,
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveSearchAttributes(self, request, context):
        """RemoveSearchAttributes removes custom search attributes.

        Returns NOT_FOUND status code if a Search Attribute with any of the specified names is not registered
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListSearchAttributes(self, request, context):
        """ListSearchAttributes returns comprehensive information about search attributes."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteNamespace(self, request, context):
        """DeleteNamespace synchronously deletes a namespace and asynchronously reclaims all namespace resources.
        (-- api-linter: core::0135::method-signature=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
        (-- api-linter: core::0135::response-message-name=disabled
        aip.dev/not-precedent: DeleteNamespace RPC doesn't follow Google API format. --)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddOrUpdateRemoteCluster(self, request, context):
        """AddOrUpdateRemoteCluster adds or updates remote cluster."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveRemoteCluster(self, request, context):
        """RemoveRemoteCluster removes remote cluster."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListClusters(self, request, context):
        """ListClusters returns information about Temporal clusters."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OperatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AddSearchAttributes": grpc.unary_unary_rpc_method_handler(
            servicer.AddSearchAttributes,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesResponse.SerializeToString,
        ),
        "RemoveSearchAttributes": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveSearchAttributes,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesResponse.SerializeToString,
        ),
        "ListSearchAttributes": grpc.unary_unary_rpc_method_handler(
            servicer.ListSearchAttributes,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesResponse.SerializeToString,
        ),
        "DeleteNamespace": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteNamespace,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceResponse.SerializeToString,
        ),
        "AddOrUpdateRemoteCluster": grpc.unary_unary_rpc_method_handler(
            servicer.AddOrUpdateRemoteCluster,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterResponse.SerializeToString,
        ),
        "RemoveRemoteCluster": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveRemoteCluster,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterResponse.SerializeToString,
        ),
        "ListClusters": grpc.unary_unary_rpc_method_handler(
            servicer.ListClusters,
            request_deserializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersRequest.FromString,
            response_serializer=temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "temporal.api.operatorservice.v1.OperatorService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OperatorService(object):
    """OperatorService API defines how Temporal SDKs and other clients interact with the Temporal server
    to perform administrative functions like registering a search attribute or a namespace.
    APIs in this file could be not compatible with Temporal Cloud, hence it's usage in SDKs should be limited by
    designated APIs that clearly state that they shouldn't be used by the main Application (Workflows & Activities) framework.
    (-- Search Attribute --)
    """

    @staticmethod
    def AddSearchAttributes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/AddSearchAttributes",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddSearchAttributesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RemoveSearchAttributes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/RemoveSearchAttributes",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveSearchAttributesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListSearchAttributes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/ListSearchAttributes",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListSearchAttributesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteNamespace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/DeleteNamespace",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.DeleteNamespaceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AddOrUpdateRemoteCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/AddOrUpdateRemoteCluster",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.AddOrUpdateRemoteClusterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RemoveRemoteCluster(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/RemoveRemoteCluster",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.RemoveRemoteClusterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListClusters(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/temporal.api.operatorservice.v1.OperatorService/ListClusters",
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersRequest.SerializeToString,
            temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2.ListClustersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import preparations_pb2 as preparations__pb2


class FederationDirectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Acknowledge_shard = channel.unary_unary(
                '/FederationDirector/Acknowledge_shard',
                request_serializer=preparations__pb2.ShardInfo.SerializeToString,
                response_deserializer=preparations__pb2.ShardAcknowledgement.FromString,
                )


class FederationDirectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Acknowledge_shard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederationDirectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Acknowledge_shard': grpc.unary_unary_rpc_method_handler(
                    servicer.Acknowledge_shard,
                    request_deserializer=preparations__pb2.ShardInfo.FromString,
                    response_serializer=preparations__pb2.ShardAcknowledgement.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FederationDirector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FederationDirector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Acknowledge_shard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/Acknowledge_shard',
            preparations__pb2.ShardInfo.SerializeToString,
            preparations__pb2.ShardAcknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

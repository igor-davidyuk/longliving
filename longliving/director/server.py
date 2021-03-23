from concurrent import futures

import logging
import grpc

from .. import preparations_pb2 
from .. import preparations_pb2_grpc

class Director(preparations_pb2_grpc.FederationDirectorServicer):
    def __init__(self, sample_shape, target_shape) -> None:
        super().__init__()
        self.sample_shape, self.target_shape = sample_shape, target_shape
        self.shard_registry = list()

    def Acknowledge_shard(self, shard_info, context):
        reply = preparations_pb2.ShardAcknowledgement(accepted=False)
        # If dataset do not match the data interface of the problem
        if (self.sample_shape != shard_info.sample_shape) or \
            (self.target_shape != shard_info.target_shape):
            return reply
        
        self.shard_registry.append(shard_info)
        print('\n\n\nRegistry now looks like this\n\n', self.shard_registry)
        reply.accepted = True
        return reply


    def serve(self):
        logging.basicConfig()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        preparations_pb2_grpc.add_FederationDirectorServicer_to_server(self, server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


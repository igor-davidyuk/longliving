import grpc

from .. import preparations_pb2 
from .. import preparations_pb2_grpc

class ClientForDirector:
    def __init__(self, shard_name, director_uri) -> None:
        self.shard_name = shard_name
        channel = grpc.insecure_channel(director_uri)
        self.stub = preparations_pb2_grpc.FederationDirectorStub(channel)


    def report_shard_info(self, shard_descriptor) -> bool:
        # True considered as successful registration 
        shard_info = preparations_pb2.ShardInfo(shard_description = shard_descriptor.dataset_description,
                            n_samples = len(shard_descriptor),
                            sample_shape = shard_descriptor.sample_shape,
                            target_shape = shard_descriptor.target_shape)

        shard_info.node_info.CopyFrom(self._get_node_info())

        acknowledgement = self.stub.Acknowledge_shard(shard_info)
        return acknowledgement.accepted

    def _get_node_info(self):
        return preparations_pb2.NodeInfo(name=self.shard_name)

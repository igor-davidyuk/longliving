import grpc
from preparations_pb2 import NodeInfo, ShardInfo, ShardAcknowledgement
from preparations_pb2_grpc import FederationDirectorStub

class ClientForDirector:
    def __init__(self, director_uri) -> None:
        channel = grpc.insecure_channel(director_uri)
        self.stub = FederationDirectorStub(channel)


    def report_shard_info(self, shard_descriptor) -> bool:
        # True considered as successful registration 
        shard_info = ShardInfo(shard_description = shard_descriptor.dataset_description,
                            n_samples = len(shard_descriptor),
                            sample_shape = shard_descriptor.sample_shape,
                            target_shape = shard_descriptor.target_shape)

        shard_info.node_info = self._get_node_info()

        acknowledgement = self.stub.AcknowledgeShard(shard_info)
        return acknowledgement.accepted

    def _get_node_info(self):
        raise NotImplementedError

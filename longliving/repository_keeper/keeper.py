from client import ClientForDirector

class RepositoryKeeper:
    def __init__(self, director_uri) -> None:
        self.director_client = ClientForDirector(director_uri)

    def start(self, shard_descriptor):
        acknowledgement = self.director_client.report_shard_info(shard_descriptor)
        if acknowledgement:
            # Shard accepted for participation in the federation
            while 1:
                # Spawn a gRPC server
                pass
        else:
            # Shut down
            pass
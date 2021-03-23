from .client import ClientForDirector

class RepositoryKeeper:
    def __init__(self, shard_name, director_uri) -> None:
        self.director_client = ClientForDirector(shard_name, director_uri)

    def start(self, shard_descriptor):
        acknowledgement = self.director_client.report_shard_info(shard_descriptor)
        if acknowledgement:
            # Shard accepted for participation in the federation
            while 1:
                # keep asking if there is an expeiment
                pass
        else:
            # Shut down
            pass
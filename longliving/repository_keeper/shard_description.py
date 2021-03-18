class ShardDescriptor:

    def __len__(self):
        raise NotImplementedError

    def get_item(self, index: int):
        # -> Tuple(np.ndarray, np.ndarray)
        raise NotImplementedError

    @property
    def sample_shape(self) -> int:
        # int( sum( [str(dim) for dim in sample.shape] ) )
        raise NotImplementedError

    @property
    def target_shape(self) -> int:
        raise NotImplementedError

    @property
    def dataset_description(self) -> str:
        return ''
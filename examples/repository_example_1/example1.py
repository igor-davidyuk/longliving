import glob
import cv2
import numpy as np
from longliving import ShardDescriptor, RepositoryKeeper

class RealShardDescriptor(ShardDescriptor):
    def __init__(self, data_path) -> None:
        super().__init__()
        self.dataset = glob.glob(data_path + '*.jpg')
        sample_item, sample_target = self.get_item(0)

        self.sample_shape = sample_item.shape
        self.target_shape = sample_target.shape


    def __len__(self):
        return len(self.dataset)

    def get_item(self, index: int):
        # -> Tuple(np.ndarray, np.ndarray)
        img = cv2.read(self.dataset[index])
        target = self.dataset[index].split('_')
        target = self._category_to_class_index(target)
        return np.array(img), np.array([target])

    @property
    def sample_shape(self) -> int:
        return int( sum( [str(dim) for dim in self.sample_shape] ) )

    @property
    def target_shape(self) -> int:
        return int( sum( [str(dim) for dim in self.target_shape] ) )

    @property
    def dataset_description(self) -> str:
        return 'Some dataset'


def main():
    data_path = '/some/path'
    shard_descriptor = RealShardDescriptor(data_path)

    director_uri = 'fqdn'
    repo_keeper = RepositoryKeeper(director_uri)
    
    repo_keeper.start(shard_descriptor)

if __name__ == '__main__':
    main()
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class RandomDatasetV2(dataset_ops.RandomDataset): ...

class RandomDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, seed: Any | None = ...) -> None: ...
RandomDataset = RandomDatasetV2
RandomDataset = RandomDatasetV1

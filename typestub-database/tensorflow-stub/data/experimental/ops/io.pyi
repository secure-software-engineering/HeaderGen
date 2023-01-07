from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import checkpoint_management as checkpoint_management, tracking as tracking
from tensorflow.python.util import lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

COMPRESSION_GZIP: str
COMPRESSION_SNAPPY: str
DATASET_SPEC_FILENAME: str
nested_structure_coder: Any

def save(dataset, path, compression: Any | None = ..., shard_func: Any | None = ..., checkpoint_args: Any | None = ...) -> None: ...

class _SaveDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, dataset, path, shard_func, compression) -> None: ...

class _LoadDataset(dataset_ops.DatasetSource):
    def __init__(self, path, element_spec: Any | None = ..., compression: Any | None = ..., reader_func: Any | None = ...): ...
    @property
    def element_spec(self): ...

def load(path, element_spec: Any | None = ..., compression: Any | None = ..., reader_func: Any | None = ...): ...

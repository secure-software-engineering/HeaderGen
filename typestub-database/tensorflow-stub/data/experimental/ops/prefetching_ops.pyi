from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import function as function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def prefetch_to_device(device, buffer_size: Any | None = ...): ...
def copy_to_device(target_device, source_device: str = ...): ...

class _CopyToDeviceDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, target_device, source_device: str = ...): ...
    def make_one_shot_iterator(self): ...

class _MapOnGpuDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset, map_func, use_inter_op_parallelism: bool = ...) -> None: ...
    @property
    def element_spec(self): ...

def map_on_gpu(map_func): ...

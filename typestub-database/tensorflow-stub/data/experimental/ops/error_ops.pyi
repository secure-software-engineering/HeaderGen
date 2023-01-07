from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

def ignore_errors(log_warning: bool = ...): ...

class _IgnoreErrorsDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, log_warning) -> None: ...

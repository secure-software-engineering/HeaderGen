from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

INFINITE: int
UNKNOWN: int

def cardinality(dataset): ...
def assert_cardinality(expected_cardinality): ...

class _AssertCardinalityDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, expected_cardinality) -> None: ...

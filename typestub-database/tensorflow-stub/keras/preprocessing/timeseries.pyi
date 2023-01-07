from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def timeseries_dataset_from_array(data, targets, sequence_length, sequence_stride: int = ..., sampling_rate: int = ..., batch_size: int = ..., shuffle: bool = ..., seed: Any | None = ..., start_index: Any | None = ..., end_index: Any | None = ...): ...
def sequences_from_indices(array, indices_ds, start_index, end_index): ...

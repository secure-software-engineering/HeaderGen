from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import distribute_lib as distribute_lib
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class DatasetCreator:
    dataset_fn: Any
    input_options: Any
    def __init__(self, dataset_fn, input_options: Any | None = ...) -> None: ...
    def __call__(self, *args, **kwargs): ...

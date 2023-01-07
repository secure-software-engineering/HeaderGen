import abc
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import data_adapter as data_adapter
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.utils import tf_utils as tf_utils, version_utils as version_utils
from tensorflow.python.ops import math_ops as math_ops, sparse_ops as sparse_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class PreprocessingLayer(Layer, metaclass=abc.ABCMeta):
    def __init__(self, streaming: bool = ..., **kwargs) -> None: ...
    @property
    def streaming(self): ...
    @property
    def is_adapted(self): ...
    def update_state(self, data) -> None: ...
    def reset_state(self) -> None: ...
    def merge_state(self, layers) -> None: ...
    def finalize_state(self) -> None: ...
    def make_adapt_function(self): ...
    def compile(self, run_eagerly: Any | None = ..., steps_per_execution: Any | None = ...) -> None: ...
    def adapt(self, data, batch_size: Any | None = ..., steps: Any | None = ..., reset_state: bool = ...) -> None: ...

class CombinerPreprocessingLayer(PreprocessingLayer):
    state_variables: Any
    def __init__(self, combiner, **kwargs) -> None: ...
    def reset_state(self) -> None: ...
    def update_state(self, data) -> None: ...
    def merge_state(self, layers) -> None: ...
    def finalize_state(self) -> None: ...
    def compile(self, run_eagerly: Any | None = ..., steps_per_execution: Any | None = ...) -> None: ...
    def adapt(self, data, batch_size: Any | None = ..., steps: Any | None = ..., reset_state: bool = ...) -> None: ...

def convert_to_list(values, sparse_default_value: Any | None = ...): ...

class Combiner(metaclass=abc.ABCMeta):
    __metaclass__: Any
    @abc.abstractmethod
    def compute(self, batch_values, accumulator: Any | None = ...): ...
    @abc.abstractmethod
    def merge(self, accumulators): ...
    @abc.abstractmethod
    def extract(self, accumulator): ...
    @abc.abstractmethod
    def restore(self, output): ...
    @abc.abstractmethod
    def serialize(self, accumulator): ...
    @abc.abstractmethod
    def deserialize(self, encoded_accumulator): ...

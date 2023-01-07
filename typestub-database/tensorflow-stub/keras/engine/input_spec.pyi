from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras import backend as backend
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export, tf_export as tf_export
from typing import Any

class InputSpec:
    dtype: Any
    ndim: Any
    shape: Any
    max_ndim: Any
    min_ndim: Any
    name: Any
    allow_last_axis_squeeze: Any
    axes: Any
    def __init__(self, dtype: Any | None = ..., shape: Any | None = ..., ndim: Any | None = ..., max_ndim: Any | None = ..., min_ndim: Any | None = ..., axes: Any | None = ..., allow_last_axis_squeeze: bool = ..., name: Any | None = ...) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

def to_tensor_shape(spec): ...
def assert_input_compatibility(input_spec, inputs, layer_name) -> None: ...
def display_shape(shape): ...
def to_tensor_spec(input_spec, default_dtype: Any | None = ...): ...

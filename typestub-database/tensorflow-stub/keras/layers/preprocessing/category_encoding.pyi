from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.keras.utils import layer_utils as layer_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, bincount_ops as bincount_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, sparse_ops as sparse_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

INT: str
ONE_HOT: str
MULTI_HOT: str
COUNT: str

class CategoryEncoding(base_layer.Layer):
    num_tokens: Any
    output_mode: Any
    sparse: Any
    def __init__(self, num_tokens: Any | None = ..., output_mode=..., sparse: bool = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...
    def call(self, inputs, count_weights: Any | None = ...): ...

def sparse_bincount(inputs, out_depth, binary_output, count_weights: Any | None = ...): ...
def dense_bincount(inputs, out_depth, binary_output, count_weights: Any | None = ...): ...

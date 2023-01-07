from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.utils import control_flow_util as control_flow_util
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops, nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class BaseDenseAttention(Layer):
    causal: Any
    dropout: Any
    supports_masking: bool
    def __init__(self, causal: bool = ..., dropout: float = ..., **kwargs) -> None: ...
    def call(self, inputs, mask: Any | None = ..., training: Any | None = ..., return_attention_scores: bool = ...): ...
    def compute_mask(self, inputs, mask: Any | None = ...): ...
    def get_config(self): ...

class Attention(BaseDenseAttention):
    use_scale: Any
    def __init__(self, use_scale: bool = ..., **kwargs) -> None: ...
    scale: Any
    def build(self, input_shape) -> None: ...
    def get_config(self): ...

class AdditiveAttention(BaseDenseAttention):
    use_scale: Any
    def __init__(self, use_scale: bool = ..., **kwargs) -> None: ...
    scale: Any
    def build(self, input_shape) -> None: ...
    def get_config(self): ...

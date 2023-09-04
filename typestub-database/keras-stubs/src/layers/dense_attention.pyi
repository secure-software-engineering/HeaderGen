from typing import Any

from keras import backend as backend
from keras.src.engine import base_layer as base_layer
from keras.utils import control_flow_util as control_flow_util

class BaseDenseAttention(base_layer.BaseRandomLayer):
    causal: Any
    dropout: Any
    supports_masking: bool
    def __init__(self, causal: bool = ..., dropout: float = ..., **kwargs) -> None: ...
    def call(
        self,
        inputs,
        mask: Any | None = ...,
        training: Any | None = ...,
        return_attention_scores: bool = ...,
    ): ...
    def compute_mask(self, inputs, mask: Any | None = ...): ...
    def compute_output_shape(self, input_shape): ...
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

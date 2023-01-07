from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn_ops as nn_ops, random_ops as random_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.util import nest as nest
from typing import Any

class DropoutWrapperBase:
    def __init__(self, cell, input_keep_prob: float = ..., output_keep_prob: float = ..., state_keep_prob: float = ..., variational_recurrent: bool = ..., input_size: Any | None = ..., dtype: Any | None = ..., seed: Any | None = ..., dropout_state_filter_visitor: Any | None = ..., **kwargs): ...
    @property
    def wrapped_cell(self): ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class ResidualWrapperBase:
    def __init__(self, cell, residual_fn: Any | None = ..., **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class DeviceWrapperBase:
    def __init__(self, cell, device, **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...

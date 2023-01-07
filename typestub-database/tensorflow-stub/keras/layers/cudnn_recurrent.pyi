from tensorflow.python.framework import constant_op as constant_op
from tensorflow.python.keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers import recurrent_v2 as recurrent_v2
from tensorflow.python.keras.layers.recurrent import RNN as RNN
from tensorflow.python.ops import array_ops as array_ops, gen_cudnn_rnn_ops as gen_cudnn_rnn_ops, state_ops as state_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class _CuDNNRNN(RNN):
    return_sequences: Any
    return_state: Any
    go_backwards: Any
    stateful: Any
    time_major: Any
    supports_masking: bool
    input_spec: Any
    state_spec: Any
    constants_spec: Any
    def __init__(self, return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., time_major: bool = ..., **kwargs) -> None: ...
    def call(self, inputs, mask: Any | None = ..., training: Any | None = ..., initial_state: Any | None = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def losses(self): ...
    def get_losses_for(self, inputs: Any | None = ...): ...

class CuDNNGRU(_CuDNNRNN):
    units: Any
    kernel_initializer: Any
    recurrent_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    recurrent_regularizer: Any
    bias_regularizer: Any
    activity_regularizer: Any
    kernel_constraint: Any
    recurrent_constraint: Any
    bias_constraint: Any
    def __init__(self, units, kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., recurrent_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., recurrent_constraint: Any | None = ..., bias_constraint: Any | None = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., **kwargs) -> None: ...
    @property
    def cell(self): ...
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def get_config(self): ...

class CuDNNLSTM(_CuDNNRNN):
    units: Any
    kernel_initializer: Any
    recurrent_initializer: Any
    bias_initializer: Any
    unit_forget_bias: Any
    kernel_regularizer: Any
    recurrent_regularizer: Any
    bias_regularizer: Any
    activity_regularizer: Any
    kernel_constraint: Any
    recurrent_constraint: Any
    bias_constraint: Any
    def __init__(self, units, kernel_initializer: str = ..., recurrent_initializer: str = ..., bias_initializer: str = ..., unit_forget_bias: bool = ..., kernel_regularizer: Any | None = ..., recurrent_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., recurrent_constraint: Any | None = ..., bias_constraint: Any | None = ..., return_sequences: bool = ..., return_state: bool = ..., go_backwards: bool = ..., stateful: bool = ..., **kwargs) -> None: ...
    @property
    def cell(self): ...
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape): ...
    def get_config(self): ...

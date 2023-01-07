from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _CudnnRNNOutput(NamedTuple):
    output: Any
    output_h: Any
    output_c: Any
    reserve_space: Any

def cudnn_rnn(input, input_h, input_c, params, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., is_training: bool = ..., name: Any | None = ...): ...

CudnnRNN: Any

def cudnn_rnn_eager_fallback(input, input_h, input_c, params, rnn_mode, input_mode, direction, dropout, seed, seed2, is_training, name, ctx): ...

class _CudnnRNNBackpropOutput(NamedTuple):
    input_backprop: Any
    input_h_backprop: Any
    input_c_backprop: Any
    params_backprop: Any

def cudnn_rnn_backprop(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

CudnnRNNBackprop: Any

def cudnn_rnn_backprop_eager_fallback(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNBackpropV2Output(NamedTuple):
    input_backprop: Any
    input_h_backprop: Any
    input_c_backprop: Any
    params_backprop: Any

def cudnn_rnn_backprop_v2(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

CudnnRNNBackpropV2: Any

def cudnn_rnn_backprop_v2_eager_fallback(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNBackpropV3Output(NamedTuple):
    input_backprop: Any
    input_h_backprop: Any
    input_c_backprop: Any
    params_backprop: Any

def cudnn_rnn_backprop_v3(input, input_h, input_c, params, sequence_lengths, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., time_major: bool = ..., name: Any | None = ...): ...

CudnnRNNBackpropV3: Any

def cudnn_rnn_backprop_v3_eager_fallback(input, input_h, input_c, params, sequence_lengths, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, host_reserved, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, time_major, name, ctx): ...
def cudnn_rnn_canonical_to_params(num_layers, num_units, input_size, weights, biases, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

CudnnRNNCanonicalToParams: Any

def cudnn_rnn_canonical_to_params_eager_fallback(num_layers, num_units, input_size, weights, biases, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...
def cudnn_rnn_canonical_to_params_v2(num_layers, num_units, input_size, weights, biases, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Any | None = ...): ...

CudnnRNNCanonicalToParamsV2: Any

def cudnn_rnn_canonical_to_params_v2_eager_fallback(num_layers, num_units, input_size, weights, biases, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...
def cudnn_rnn_params_size(num_layers, num_units, input_size, T, S, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Any | None = ...): ...

CudnnRNNParamsSize: Any

def cudnn_rnn_params_size_eager_fallback(num_layers, num_units, input_size, T, S, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...

class _CudnnRNNParamsToCanonicalOutput(NamedTuple):
    weights: Any
    biases: Any

def cudnn_rnn_params_to_canonical(num_layers, num_units, input_size, params, num_params, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

CudnnRNNParamsToCanonical: Any

def cudnn_rnn_params_to_canonical_eager_fallback(num_layers, num_units, input_size, params, num_params, rnn_mode, input_mode, direction, dropout, seed, seed2, name, ctx): ...

class _CudnnRNNParamsToCanonicalV2Output(NamedTuple):
    weights: Any
    biases: Any

def cudnn_rnn_params_to_canonical_v2(num_layers, num_units, input_size, params, num_params_weights, num_params_biases, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., name: Any | None = ...): ...

CudnnRNNParamsToCanonicalV2: Any

def cudnn_rnn_params_to_canonical_v2_eager_fallback(num_layers, num_units, input_size, params, num_params_weights, num_params_biases, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, name, ctx): ...

class _CudnnRNNV2Output(NamedTuple):
    output: Any
    output_h: Any
    output_c: Any
    reserve_space: Any
    host_reserved: Any

def cudnn_rnnv2(input, input_h, input_c, params, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., is_training: bool = ..., name: Any | None = ...): ...

CudnnRNNV2: Any

def cudnn_rnnv2_eager_fallback(input, input_h, input_c, params, rnn_mode, input_mode, direction, dropout, seed, seed2, is_training, name, ctx): ...

class _CudnnRNNV3Output(NamedTuple):
    output: Any
    output_h: Any
    output_c: Any
    reserve_space: Any
    host_reserved: Any

def cudnn_rnnv3(input, input_h, input_c, params, sequence_lengths, rnn_mode: str = ..., input_mode: str = ..., direction: str = ..., dropout: int = ..., seed: int = ..., seed2: int = ..., num_proj: int = ..., is_training: bool = ..., time_major: bool = ..., name: Any | None = ...): ...

CudnnRNNV3: Any

def cudnn_rnnv3_eager_fallback(input, input_h, input_c, params, sequence_lengths, rnn_mode, input_mode, direction, dropout, seed, seed2, num_proj, is_training, time_major, name, ctx): ...

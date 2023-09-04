import threading
import weakref
from typing import Any

import tensorflow.compat.v2 as tf
from keras import backend_config as backend_config
from keras.src.engine import keras_tensor as keras_tensor
from keras.utils import control_flow_util as control_flow_util
from keras.utils import object_identity as object_identity
from keras.utils import tf_contextlib as tf_contextlib
from keras.utils import tf_inspect as tf_inspect

py_all = all
py_sum = sum
py_any = any

class SessionLocal(threading.local):
    session: Any
    def __init__(self) -> None: ...

PER_GRAPH_OBJECT_NAME_UIDS: Any
OBSERVED_NAMES: Any

class _DummyEagerGraph(threading.local):
    class _WeakReferencableClass: ...
    key: Any
    learning_phase_is_set: bool
    def __init__(self) -> None: ...

epsilon = backend_config.epsilon
floatx = backend_config.floatx
image_data_format = backend_config.image_data_format
set_epsilon = backend_config.set_epsilon
set_floatx = backend_config.set_floatx
set_image_data_format = backend_config.set_image_data_format

def backend(): ...
def cast_to_floatx(x): ...
def get_uid(prefix: str = ...): ...
def reset_uids() -> None: ...
def clear_session() -> None: ...
def manual_variable_initialization(value) -> None: ...
def learning_phase(): ...
def global_learning_phase_is_set(): ...
def symbolic_learning_phase(): ...
def set_learning_phase(value) -> None: ...
def deprecated_internal_set_learning_phase(value) -> None: ...
def learning_phase_scope(value) -> None: ...
def deprecated_internal_learning_phase_scope(value) -> None: ...
def eager_learning_phase_scope(value) -> None: ...
def get_session(op_input_list=...): ...
def get_graph(): ...
def set_session(session) -> None: ...
def get_default_session_config(): ...
def get_default_graph_uid_map(): ...

class _TfDeviceCaptureOp:
    device: Any
    def __init__(self) -> None: ...

def is_sparse(tensor): ...
def to_dense(tensor): ...
def name_scope(name): ...
def variable(
    value, dtype: Any | None = ..., name: Any | None = ..., constraint: Any | None = ...
): ...
def track_tf_optimizer(tf_optimizer) -> None: ...
def track_variable(v) -> None: ...
def observe_object_name(name) -> None: ...
def unique_object_name(
    name,
    name_uid_map: Any | None = ...,
    avoid_names: Any | None = ...,
    namespace: str = ...,
    zero_based: bool = ...,
    avoid_observed_names: bool = ...,
): ...
def constant(
    value, dtype: Any | None = ..., shape: Any | None = ..., name: Any | None = ...
): ...
def is_keras_tensor(x): ...
def placeholder(
    shape: Any | None = ...,
    ndim: Any | None = ...,
    dtype: Any | None = ...,
    sparse: bool = ...,
    name: Any | None = ...,
    ragged: bool = ...,
): ...
def is_placeholder(x): ...
def shape(x): ...
def int_shape(x): ...
def ndim(x): ...
def dtype(x): ...
def dtype_numpy(x): ...
def eval(x): ...
def zeros(shape, dtype: Any | None = ..., name: Any | None = ...): ...
def ones(shape, dtype: Any | None = ..., name: Any | None = ...): ...
def eye(size, dtype: Any | None = ..., name: Any | None = ...): ...
def zeros_like(x, dtype: Any | None = ..., name: Any | None = ...): ...
def ones_like(x, dtype: Any | None = ..., name: Any | None = ...): ...
def identity(x, name: Any | None = ...): ...
def is_tf_random_generator_enabled(): ...
def enable_tf_random_generator() -> None: ...
def disable_tf_random_generator() -> None: ...

class RandomGenerator(tf.__internal__.tracking.AutoTrackable):
    def __init__(self, seed: Any | None = ..., force_generator: bool = ...) -> None: ...
    def make_seed_for_stateless_op(self): ...
    def make_legacy_seed(self): ...
    def random_normal(
        self, shape, mean: float = ..., stddev: float = ..., dtype: Any | None = ...
    ): ...
    def random_uniform(
        self,
        shape,
        minval: float = ...,
        maxval: Any | None = ...,
        dtype: Any | None = ...,
    ): ...
    def truncated_normal(
        self, shape, mean: float = ..., stddev: float = ..., dtype: Any | None = ...
    ): ...
    def dropout(self, inputs, rate, noise_shape: Any | None = ...): ...

def random_uniform_variable(
    shape,
    low,
    high,
    dtype: Any | None = ...,
    name: Any | None = ...,
    seed: Any | None = ...,
): ...
def random_normal_variable(
    shape,
    mean,
    scale,
    dtype: Any | None = ...,
    name: Any | None = ...,
    seed: Any | None = ...,
): ...
def count_params(x): ...
def cast(x, dtype): ...
def update(x, new_x): ...
def update_add(x, increment): ...
def update_sub(x, decrement): ...
def moving_average_update(x, value, momentum): ...
def dot(x, y): ...
def batch_dot(x, y, axes: Any | None = ...): ...
def transpose(x): ...
def gather(reference, indices): ...
def max(x, axis: Any | None = ..., keepdims: bool = ...): ...
def min(x, axis: Any | None = ..., keepdims: bool = ...): ...
def sum(x, axis: Any | None = ..., keepdims: bool = ...): ...
def prod(x, axis: Any | None = ..., keepdims: bool = ...): ...
def cumsum(x, axis: int = ...): ...
def cumprod(x, axis: int = ...): ...
def var(x, axis: Any | None = ..., keepdims: bool = ...): ...
def std(x, axis: Any | None = ..., keepdims: bool = ...): ...
def mean(x, axis: Any | None = ..., keepdims: bool = ...): ...
def any(x, axis: Any | None = ..., keepdims: bool = ...): ...
def all(x, axis: Any | None = ..., keepdims: bool = ...): ...
def argmax(x, axis: int = ...): ...
def argmin(x, axis: int = ...): ...
def square(x): ...
def abs(x): ...
def sqrt(x): ...
def exp(x): ...
def log(x): ...
def logsumexp(x, axis: Any | None = ..., keepdims: bool = ...): ...
def round(x): ...
def sign(x): ...
def pow(x, a): ...
def clip(x, min_value, max_value): ...
def equal(x, y): ...
def not_equal(x, y): ...
def greater(x, y): ...
def greater_equal(x, y): ...
def less(x, y): ...
def less_equal(x, y): ...
def maximum(x, y): ...
def minimum(x, y): ...
def sin(x): ...
def cos(x): ...
def normalize_batch_in_training(
    x, gamma, beta, reduction_axes, epsilon: float = ...
): ...
def batch_normalization(
    x, mean, var, beta, gamma, axis: int = ..., epsilon: float = ...
): ...
def concatenate(tensors, axis: int = ...): ...
def reshape(x, shape): ...
def permute_dimensions(x, pattern): ...
def resize_images(
    x, height_factor, width_factor, data_format, interpolation: str = ...
): ...
def resize_volumes(x, depth_factor, height_factor, width_factor, data_format): ...
def repeat_elements(x, rep, axis): ...
def repeat(x, n): ...
def arange(start, stop: Any | None = ..., step: int = ..., dtype: str = ...): ...
def tile(x, n): ...
def flatten(x): ...
def batch_flatten(x): ...
def expand_dims(x, axis: int = ...): ...
def squeeze(x, axis): ...
def temporal_padding(x, padding=...): ...
def spatial_2d_padding(x, padding=..., data_format: Any | None = ...): ...
def spatial_3d_padding(x, padding=..., data_format: Any | None = ...): ...
def stack(x, axis: int = ...): ...
def one_hot(indices, num_classes): ...
def reverse(x, axes): ...
def get_value(x): ...
def batch_get_value(tensors): ...
def set_value(x, value) -> None: ...
def batch_set_value(tuples) -> None: ...
def print_tensor(x, message: str = ..., summarize: int = ...): ...

class GraphExecutionFunction:
    inputs: Any
    outputs: Any
    updates_op: Any
    name: Any
    feed_dict: Any
    fetches: Any
    run_options: Any
    run_metadata: Any
    session_kwargs: Any
    fetch_callbacks: Any
    def __init__(
        self,
        inputs,
        outputs,
        updates: Any | None = ...,
        name: Any | None = ...,
        **session_kwargs
    ) -> None: ...
    def __call__(self, inputs): ...

def function(
    inputs, outputs, updates: Any | None = ..., name: Any | None = ..., **kwargs
): ...
def gradients(loss, variables): ...
def stop_gradient(variables): ...
def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards: bool = ...,
    mask: Any | None = ...,
    constants: Any | None = ...,
    unroll: bool = ...,
    input_length: Any | None = ...,
    time_major: bool = ...,
    zero_output_for_mask: bool = ...,
): ...
def switch(condition, then_expression, else_expression): ...
def in_train_phase(x, alt, training: Any | None = ...): ...
def in_test_phase(x, alt, training: Any | None = ...): ...
def relu(
    x, alpha: float = ..., max_value: Any | None = ..., threshold: float = ...
): ...
def elu(x, alpha: float = ...): ...
def softmax(x, axis: int = ...): ...
def softplus(x): ...
def softsign(x): ...
def categorical_crossentropy(
    target, output, from_logits: bool = ..., axis: int = ...
): ...
def sparse_categorical_crossentropy(
    target, output, from_logits: bool = ..., axis: int = ...
): ...
def binary_crossentropy(target, output, from_logits: bool = ...): ...
def binary_focal_crossentropy(
    target, output, gamma: float = ..., from_logits: bool = ...
): ...
def binary_weighted_focal_crossentropy(
    target, output, alpha: float = ..., gamma: float = ..., from_logits: bool = ...
): ...
def sigmoid(x): ...
def hard_sigmoid(x): ...
def tanh(x): ...
def dropout(x, level, noise_shape: Any | None = ..., seed: Any | None = ...): ...
def l2_normalize(x, axis: Any | None = ...): ...
def in_top_k(predictions, targets, k): ...
def conv1d(
    x,
    kernel,
    strides: int = ...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate: int = ...,
): ...
def conv2d(
    x,
    kernel,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate=...,
): ...
def conv2d_transpose(
    x,
    kernel,
    output_shape,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate=...,
): ...
def separable_conv1d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides: int = ...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate: int = ...,
): ...
def separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate=...,
): ...
def depthwise_conv2d(
    x,
    depthwise_kernel,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate=...,
): ...
def conv3d(
    x,
    kernel,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    dilation_rate=...,
): ...
def conv3d_transpose(
    x,
    kernel,
    output_shape,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
): ...
def pool2d(
    x,
    pool_size,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    pool_mode: str = ...,
): ...
def pool3d(
    x,
    pool_size,
    strides=...,
    padding: str = ...,
    data_format: Any | None = ...,
    pool_mode: str = ...,
): ...
def local_conv(
    inputs, kernel, kernel_size, strides, output_shape, data_format: Any | None = ...
): ...
def local_conv1d(
    inputs, kernel, kernel_size, strides, data_format: Any | None = ...
): ...
def local_conv2d(
    inputs, kernel, kernel_size, strides, output_shape, data_format: Any | None = ...
): ...
def bias_add(x, bias, data_format: Any | None = ...): ...
def random_normal(
    shape,
    mean: float = ...,
    stddev: float = ...,
    dtype: Any | None = ...,
    seed: Any | None = ...,
): ...
def random_uniform(
    shape,
    minval: float = ...,
    maxval: float = ...,
    dtype: Any | None = ...,
    seed: Any | None = ...,
): ...
def random_binomial(
    shape, p: float = ..., dtype: Any | None = ..., seed: Any | None = ...
): ...
def random_bernoulli(
    shape, p: float = ..., dtype: Any | None = ..., seed: Any | None = ...
): ...
def truncated_normal(
    shape,
    mean: float = ...,
    stddev: float = ...,
    dtype: Any | None = ...,
    seed: Any | None = ...,
): ...
def ctc_label_dense_to_sparse(labels, label_lengths): ...
def ctc_batch_cost(y_true, y_pred, input_length, label_length): ...
def ctc_decode(
    y_pred,
    input_length,
    greedy: bool = ...,
    beam_width: int = ...,
    top_paths: int = ...,
): ...
def map_fn(fn, elems, name: Any | None = ..., dtype: Any | None = ...): ...
def foldl(fn, elems, initializer: Any | None = ..., name: Any | None = ...): ...
def foldr(fn, elems, initializer: Any | None = ..., name: Any | None = ...): ...
def configure_and_create_distributed_session(distribution_strategy) -> None: ...
def is_tpu_strategy(strategy): ...
def cast_variables_to_tensor(tensors): ...
def convert_inputs_if_ragged(inputs): ...
def maybe_convert_to_ragged(
    is_ragged_input, output, nested_row_lengths, go_backwards: bool = ...
): ...

class ContextValueCache(weakref.WeakKeyDictionary):
    default_factory: Any
    def __init__(self, default_factory) -> None: ...
    def __getitem__(self, key): ...
    def setdefault(
        self, key: Any | None = ..., default: Any | None = ..., kwargs: Any | None = ...
    ): ...

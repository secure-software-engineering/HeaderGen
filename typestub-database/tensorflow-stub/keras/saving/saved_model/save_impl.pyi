import threading
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils, input_spec as input_spec
from tensorflow.python.keras.mixed_precision import autocast_variable as autocast_variable
from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import constants as constants, serialized_attributes as serialized_attributes, utils as utils
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib, tf_inspect as tf_inspect, tf_utils as tf_utils, version_utils as version_utils
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.training.tracking import data_structures as data_structures
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator
from typing import Any

base_layer: Any
metrics: Any
input_layer: Any
training_lib: Any
sequential_lib: Any

def should_skip_serialization(layer): ...
def wrap_layer_objects(layer, serialization_cache): ...
def wrap_layer_functions(layer, serialization_cache): ...
def default_save_signature(layer): ...

class LayerTracingContext(threading.local):
    enable_call_tracing: bool
    trace_queue: Any
    def __init__(self) -> None: ...

def tracing_scope() -> None: ...
def add_trace_to_queue(fn, args, kwargs, training: Any | None = ...) -> None: ...
def tracing_enabled(): ...

class LayerCallCollection:
    layer: Any
    layer_call_method: Any
    def __init__(self, layer) -> None: ...
    def add_trace(self, *args, **kwargs) -> None: ...
    @property
    def fn_input_signature(self): ...
    def training_arg_was_passed(self, args, kwargs): ...
    def get_training_arg_value(self, args, kwargs): ...
    def get_input_arg_value(self, args, kwargs): ...
    def add_function(self, call_fn, name, match_layer_training_arg): ...
    def trace_with_input_signature(self) -> None: ...

def layer_call_wrapper(call_collection, method, name): ...

class LayerCall:
    call_collection: Any
    input_signature: Any
    wrapped_call: Any
    original_layer_call: Any
    def __init__(self, call_collection, call_fn, name, input_signature) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def get_concrete_function(self, *args, **kwargs): ...

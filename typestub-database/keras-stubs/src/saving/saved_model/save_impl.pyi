import threading
from typing import Any

from keras import backend as backend
from keras.mixed_precision import autocast_variable as autocast_variable
from keras.src.engine import base_layer_utils as base_layer_utils
from keras.src.engine import input_spec as input_spec
from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import constants as constants
from keras.src.saving.saved_model import serialized_attributes as serialized_attributes
from keras.src.saving.saved_model import utils as utils
from keras.utils import tf_contextlib as tf_contextlib
from keras.utils import tf_inspect as tf_inspect
from keras.utils import tf_utils as tf_utils
from keras.utils import version_utils as version_utils
from keras.utils.generic_utils import LazyLoader as LazyLoader

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
    def training_arg_was_passed(self, args, kwargs): ...
    def get_training_arg_value(self, args, kwargs): ...
    def get_input_arg_value(self, args, kwargs): ...
    def add_function(self, call_fn, name, match_layer_training_arg): ...
    def trace_with_input_signature(self) -> None: ...

def layer_call_wrapper(call_collection, method, name): ...

class LayerCall:
    call_collection: Any
    wrapped_call: Any
    original_layer_call: Any
    def __init__(self, call_collection, call_fn, name) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def get_concrete_function(self, *args, **kwargs): ...

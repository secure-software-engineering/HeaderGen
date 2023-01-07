from tensorflow.python.util import lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

constant_op: Any

def register_tensor_conversion_function(base_type, conversion_func, priority: int = ...) -> None: ...
def get(query): ...

from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class _XlaScope:
    count: Any
    depth: Any
    def __init__(self, count, depth) -> None: ...

def experimental_jit_scope(compile_ops: bool = ..., separate_compiled_gradients: bool = ...): ...

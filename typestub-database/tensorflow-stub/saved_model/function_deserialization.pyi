from tensorflow.core.framework import function_pb2 as function_pb2
from tensorflow.core.protobuf import saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import op_def_registry as op_def_registry, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import custom_gradient as custom_gradient, default_gradient as default_gradient, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import compat as compat, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any

def setup_bare_concrete_function(saved_bare_concrete_function, concrete_functions): ...

class RestoredFunction(def_function.Function):
    concrete_functions: Any
    def __init__(self, python_function, name, function_spec, concrete_functions) -> None: ...

def recreate_function(saved_function, concrete_functions): ...
def load_function_def_library(library, load_shared_name_suffix: Any | None = ..., wrapper_function: Any | None = ...): ...
def fix_node_def(node_def, functions, shared_name_suffix) -> None: ...

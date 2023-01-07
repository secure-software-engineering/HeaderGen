from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import backprop as backprop, backprop_util as backprop_util, context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_state as control_flow_state, control_flow_util as control_flow_util, default_gradient as default_gradient, functional_ops as functional_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import compat as compat, object_identity as object_identity
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class AggregationMethod:
    ADD_N: int
    DEFAULT: Any
    EXPERIMENTAL_TREE: int
    EXPERIMENTAL_ACCUMULATE_N: int

POSSIBLE_GRADIENT_TYPES_NONE: int
POSSIBLE_GRADIENT_TYPES_FIRST_ORDER: int
POSSIBLE_GRADIENT_TYPES_HIGHER_ORDER: int

def PossibleTapeGradientTypes(tensors): ...

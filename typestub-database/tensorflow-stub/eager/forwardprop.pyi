from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import backprop as backprop, backprop_util as backprop_util, execute as execute, forwardprop_util as forwardprop_util, function as function
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.ops.parallel_for import control_flow_ops as control_flow_ops
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class ForwardAccumulator:
    def __init__(self, primals, tangents) -> None: ...
    def __enter__(self): ...
    def __exit__(self, typ, value, traceback) -> None: ...
    def jvp(self, primals, unconnected_gradients=...): ...

from tensorflow.python.compat import compat as compat
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_math_ops as gen_math_ops, math_ops as math_ops, special_math_ops as special_math_ops

def SmartBroadcastGradientArgs(x, y, grad): ...

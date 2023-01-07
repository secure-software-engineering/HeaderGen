from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import control_flow_ops as control_flow_ops, variables as variables
from typing import Any

def InXlaContext(graph): ...
def GraphOrParentsInXlaContext(graph): ...
def IsInWhileLoop(op): ...
def GetContainingWhileContext(ctxt, stop_ctxt: Any | None = ...): ...
def GetContainingXLAContext(ctxt): ...
def smart_cond(pred, true_fn: Any | None = ..., false_fn: Any | None = ..., name: Any | None = ...): ...
def constant_value(pred): ...

from tensorflow.python.framework import func_graph as func_graph, ops as ops

class ControlFlowFuncGraph(func_graph.FuncGraph):
    is_control_flow_graph: bool
    def __init__(self, *args, **kwargs) -> None: ...

class CondBranchFuncGraph(ControlFlowFuncGraph): ...
class WhileCondFuncGraph(ControlFlowFuncGraph): ...
class WhileBodyFuncGraph(ControlFlowFuncGraph): ...

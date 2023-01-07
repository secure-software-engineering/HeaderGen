from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, transformer as transformer
from typing import Any

class Definition:
    param_of: Any
    directives: Any
    def __init__(self) -> None: ...

class _NodeState:
    value: Any
    def __init__(self, init_from: Any | None = ...) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __or__(self, other): ...
    def __sub__(self, other): ...

class Analyzer(cfg.GraphVisitor):
    gen_map: Any
    def __init__(self, graph, definition_factory) -> None: ...
    def init_state(self, _): ...
    def visit_node(self, node): ...

class TreeAnnotator(transformer.Base):
    allow_skips: bool
    definition_factory: Any
    graphs: Any
    current_analyzer: Any
    current_cfg_node: Any
    def __init__(self, source_info, graphs, definition_factory) -> None: ...
    def visit_FunctionDef(self, node): ...
    def visit_Name(self, node): ...
    def visit_If(self, node): ...
    def visit_For(self, node): ...
    def visit_While(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...
    def visit(self, node): ...

def resolve(node, source_info, graphs, definition_factory=...): ...

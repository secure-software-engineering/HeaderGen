import gast
from typing import Any

class PrettyPrinter(gast.NodeVisitor):
    indent_lvl: int
    result: str
    color: Any
    noanno: Any
    def __init__(self, color, noanno) -> None: ...
    def generic_visit(self, node, name: Any | None = ...) -> None: ...

def fmt(node, color: bool = ..., noanno: bool = ...): ...

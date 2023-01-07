from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno
from typing import Any

class _Break:
    used: bool
    control_var_name: Any
    def __init__(self) -> None: ...

class BreakTransformer(converter.Base):
    def visit_Break(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...

def transform(node, ctx): ...

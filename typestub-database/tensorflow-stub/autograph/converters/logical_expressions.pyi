from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import parser as parser, templates as templates
from typing import Any

SAFE_BOOLEAN_OPERAND: str
LOGICAL_OPERATORS: Any
EQUALITY_OPERATORS: Any

class LogicalExpressionTransformer(converter.Base):
    def visit_Compare(self, node): ...
    def visit_UnaryOp(self, node): ...
    def visit_BoolOp(self, node): ...

def transform(node, ctx): ...

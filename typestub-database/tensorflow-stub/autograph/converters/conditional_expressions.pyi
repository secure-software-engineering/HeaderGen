from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import parser as parser, templates as templates

class ConditionalExpressionTransformer(converter.Base):
    def visit_IfExp(self, node): ...

def transform(node, ctx): ...

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import templates as templates

class ListCompTransformer(converter.Base):
    def visit_Assign(self, node): ...

def transform(node, ctx): ...

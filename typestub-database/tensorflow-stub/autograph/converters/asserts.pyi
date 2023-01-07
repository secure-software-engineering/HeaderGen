from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import templates as templates

class AssertTransformer(converter.Base):
    def visit_Assert(self, node): ...

def transform(node, ctx): ...

from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, templates as templates

class VariableAccessTransformer(converter.Base):
    def visit_Name(self, node): ...
    def visit_Delete(self, node): ...
    def visit_AugAssign(self, node): ...

def transform(node, ctx): ...

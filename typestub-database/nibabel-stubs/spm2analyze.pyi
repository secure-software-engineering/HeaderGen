from _typeshed import Incomplete

from . import spm99analyze as spm99

image_dimension_dtd: Incomplete
header_dtype: Incomplete

class Spm2AnalyzeHeader(spm99.Spm99AnalyzeHeader):
    template_dtype = header_dtype
    def get_slope_inter(self): ...
    @classmethod
    def may_contain_header(klass, binaryblock): ...

class Spm2AnalyzeImage(spm99.Spm99AnalyzeImage):
    header_class = Spm2AnalyzeHeader
    header: Spm2AnalyzeHeader

load: Incomplete
save: Incomplete

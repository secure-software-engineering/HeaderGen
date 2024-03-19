from ..spatialimages import HeaderDataError as HeaderDataError
from ..spatialimages import HeaderTypeError as HeaderTypeError
from ..spm2analyze import Spm2AnalyzeHeader as Spm2AnalyzeHeader
from ..spm2analyze import Spm2AnalyzeImage as Spm2AnalyzeImage
from . import test_spm99analyze as test_spm99analyze

class TestSpm2AnalyzeHeader(test_spm99analyze.TestSpm99AnalyzeHeader):
    header_class = Spm2AnalyzeHeader
    def test_slope_inter(self) -> None: ...

class TestSpm2AnalyzeImage(test_spm99analyze.TestSpm99AnalyzeImage):
    image_class = Spm2AnalyzeImage

def test_origin_affine() -> None: ...

from _typeshed import Incomplete

from . import analyze as analyze
from .batteryrunners import Report as Report
from .optpkg import optional_package as optional_package
from .spatialimages import HeaderDataError as HeaderDataError
from .spatialimages import HeaderTypeError as HeaderTypeError

have_scipy: Incomplete
header_key_dtd: Incomplete
image_dimension_dtd: Incomplete
data_history_dtd: Incomplete
header_dtype: Incomplete

class SpmAnalyzeHeader(analyze.AnalyzeHeader):
    template_dtype = header_dtype
    has_data_slope: bool
    has_data_intercept: bool
    @classmethod
    def default_structarr(klass, endianness: Incomplete | None = None): ...
    def get_slope_inter(self): ...
    def set_slope_inter(self, slope, inter: Incomplete | None = None) -> None: ...

class Spm99AnalyzeHeader(SpmAnalyzeHeader):
    def get_origin_affine(self): ...
    get_best_affine = get_origin_affine
    def set_origin_from_affine(self, affine) -> None: ...

class Spm99AnalyzeImage(analyze.AnalyzeImage):
    header_class = Spm99AnalyzeHeader
    header: Spm99AnalyzeHeader
    files_types: Incomplete
    has_affine: bool
    makeable: bool
    rw = have_scipy
    @classmethod
    def from_file_map(
        klass, file_map, *, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...
    def to_file_map(
        self, file_map: Incomplete | None = None, dtype: Incomplete | None = None
    ) -> None: ...

load: Incomplete
save: Incomplete

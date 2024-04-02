from _typeshed import Incomplete

from ..casting import sctypes_aliases as sctypes_aliases
from ..casting import shared_range as shared_range
from ..casting import type_info as type_info
from ..optpkg import optional_package as optional_package
from ..spatialimages import HeaderDataError as HeaderDataError
from ..spm99analyze import HeaderTypeError as HeaderTypeError
from ..spm99analyze import Spm99AnalyzeHeader as Spm99AnalyzeHeader
from ..spm99analyze import Spm99AnalyzeImage as Spm99AnalyzeImage
from ..testing import assert_allclose_safely as assert_allclose_safely
from ..testing import bytesio_filemap as bytesio_filemap
from ..testing import bytesio_round_trip as bytesio_round_trip
from ..testing import suppress_warnings as suppress_warnings
from ..volumeutils import apply_read_scaling as apply_read_scaling
from . import test_analyze as test_analyze

_: Incomplete
have_scipy: Incomplete
needs_scipy: Incomplete
sctypes: Incomplete
FLOAT_TYPES: Incomplete
COMPLEX_TYPES: Incomplete
INT_TYPES: Incomplete
UINT_TYPES: Incomplete
CFLOAT_TYPES: Incomplete
IUINT_TYPES: Incomplete
NUMERIC_TYPES: Incomplete

class HeaderScalingMixin:
    def test_data_scaling(self) -> None: ...

class TestSpm99AnalyzeHeader(test_analyze.TestAnalyzeHeader, HeaderScalingMixin):
    header_class = Spm99AnalyzeHeader
    def test_empty(self) -> None: ...
    def test_big_scaling(self) -> None: ...
    def test_slope_inter(self) -> None: ...
    def test_origin_checks(self) -> None: ...

class ImageScalingMixin:
    def assert_scaling_equal(self, hdr, slope, inter) -> None: ...
    def assert_scale_me_scaling(self, hdr) -> None: ...
    def assert_null_scaling(self, arr, slope, inter) -> None: ...
    def test_header_scaling(self) -> None: ...
    def test_int_int_scaling(self) -> None: ...
    def test_no_scaling(self, in_dtype, supported_dtype) -> None: ...
    def test_write_scaling(self) -> None: ...
    def test_nan2zero_range_ok(self) -> None: ...

class TestSpm99AnalyzeImage(test_analyze.TestAnalyzeImage, ImageScalingMixin):
    image_class = Spm99AnalyzeImage
    test_data_hdr_cache: Incomplete
    test_header_updating: Incomplete
    test_offset_to_zero: Incomplete
    test_big_offset_exts: Incomplete
    test_dtype_to_filename_arg: Incomplete
    test_header_scaling: Incomplete
    test_int_int_scaling: Incomplete
    test_write_scaling: Incomplete
    test_no_scaling: Incomplete
    test_nan2zero_range_ok: Incomplete
    def test_mat_read(self) -> None: ...
    def test_none_affine(self) -> None: ...

def test_origin_affine() -> None: ...

from _typeshed import Incomplete
from nibabel.testing import assert_allclose_safely as assert_allclose_safely
from nibabel.testing import assert_dt_equal as assert_dt_equal
from nibabel.testing import error_warnings as error_warnings
from nibabel.testing import suppress_warnings as suppress_warnings

from ..casting import OK_FLOATS as OK_FLOATS
from ..casting import floor_log2 as floor_log2
from ..casting import sctypes as sctypes
from ..casting import shared_range as shared_range
from ..casting import type_info as type_info
from ..openers import BZ2File as BZ2File
from ..openers import ImageOpener as ImageOpener
from ..openers import Opener as Opener
from ..optpkg import optional_package as optional_package
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from ..volumeutils import apply_read_scaling as apply_read_scaling
from ..volumeutils import array_from_file as array_from_file
from ..volumeutils import array_to_file as array_to_file
from ..volumeutils import best_write_scale_ftype as best_write_scale_ftype
from ..volumeutils import better_float_of as better_float_of
from ..volumeutils import fname_ext_ul_case as fname_ext_ul_case
from ..volumeutils import int_scinter_ftype as int_scinter_ftype
from ..volumeutils import make_dt_codes as make_dt_codes
from ..volumeutils import native_code as native_code
from ..volumeutils import rec2dict as rec2dict
from ..volumeutils import seek_tell as seek_tell
from ..volumeutils import shape_zoom_affine as shape_zoom_affine
from ..volumeutils import working_type as working_type
from ..volumeutils import write_zeros as write_zeros

pyzstd: Incomplete
HAVE_ZSTD: Incomplete
_: Incomplete
FLOAT_TYPES: Incomplete
COMPLEX_TYPES: Incomplete
CFLOAT_TYPES: Incomplete
INT_TYPES: Incomplete
IUINT_TYPES: Incomplete
NUMERIC_TYPES: Incomplete
FP_RUNTIME_WARN: Incomplete
NP_2: Incomplete

def test__is_compressed_fobj() -> None: ...
def test_fobj_string_assumptions(): ...
def test_array_from_file() -> None: ...
def test_array_from_file_mmap() -> None: ...
def buf_chk(in_arr, out_buf, in_buf, offset): ...
def test_array_from_file_openers() -> None: ...
def test_array_from_file_reread() -> None: ...
def test_array_to_file() -> None: ...
def test_a2f_intercept_scale() -> None: ...
def test_a2f_upscale() -> None: ...
def test_a2f_min_max() -> None: ...
def test_a2f_order() -> None: ...
def test_a2f_nan2zero() -> None: ...
def test_a2f_nan2zero_scaling() -> None: ...
def test_a2f_offset() -> None: ...
def test_a2f_dtype_default() -> None: ...
def test_a2f_zeros() -> None: ...
def test_a2f_big_scalers() -> None: ...
def test_a2f_int_scaling() -> None: ...
def test_a2f_scaled_unscaled() -> None: ...
def test_a2f_nanpos() -> None: ...
def test_a2f_bad_scaling() -> None: ...
def test_a2f_nan2zero_range() -> None: ...
def test_a2f_non_numeric() -> None: ...
def write_return(data, fileobj, out_dtype, *args, **kwargs): ...
def test_apply_scaling() -> None: ...
def test_apply_read_scaling_ints() -> None: ...
def test_apply_read_scaling_nones() -> None: ...
def test_int_scinter() -> None: ...
def test_working_type(): ...
def test_better_float(): ...
def test_best_write_scale_ftype() -> None: ...
def test_write_zeros() -> None: ...
def test_seek_tell() -> None: ...
def test_seek_tell_logic() -> None: ...
def test_fname_ext_ul_case() -> None: ...
def test_shape_zoom_affine() -> None: ...
def test_rec2dict() -> None: ...
def test_dtypes() -> None: ...
def test__write_data() -> None: ...
def test_array_from_file_overflow(): ...
def test__ftype4scaled_finite_warningfilters() -> None: ...

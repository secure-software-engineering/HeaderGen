from collections.abc import Generator

from _typeshed import Incomplete

from .. import __version__ as __version__
from ..arrayproxy import ArrayProxy as ArrayProxy
from ..arrayproxy import get_obj_dtype as get_obj_dtype
from ..arrayproxy import is_proxy as is_proxy
from ..arrayproxy import reshape_dataobj as reshape_dataobj
from ..deprecator import ExpiredDeprecationError as ExpiredDeprecationError
from ..nifti1 import Nifti1Header as Nifti1Header
from ..nifti1 import Nifti1Image as Nifti1Image
from ..openers import ImageOpener as ImageOpener
from ..testing import memmap_after_ufunc as memmap_after_ufunc
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from .test_fileslice import slicer_samples as slicer_samples
from .test_openers import patch_indexed_gzip as patch_indexed_gzip

class FunkyHeader:
    shape: Incomplete
    def __init__(self, shape) -> None: ...
    def get_data_shape(self): ...
    def get_data_dtype(self): ...
    def get_data_offset(self): ...
    def get_slope_inter(self): ...
    def copy(self): ...

class CArrayProxy(ArrayProxy): ...

class DeprecatedCArrayProxy(ArrayProxy):
    order: str

def test_init() -> None: ...
def test_tuplespec() -> None: ...
def write_raw_data(arr, hdr, fileobj) -> None: ...
def test_nifti1_init() -> None: ...
def test_proxy_slicing(n_dim, offset) -> None: ...
def test_proxy_slicing_with_scaling() -> None: ...
def test_order_override(order) -> None: ...
def test_deprecated_order_classvar() -> None: ...
def test_is_proxy() -> None: ...
def test_reshape_dataobj(): ...
def test_reshaped_is_proxy() -> None: ...
def test_get_obj_dtype(): ...
def test_get_unscaled(): ...
def test_mmap() -> None: ...
def check_mmap(
    hdr, offset, proxy_class, has_scaling: bool = False, unscaled_is_view: bool = True
) -> None: ...

class CountingImageOpener(ImageOpener):
    num_openers: int
    def __init__(self, *args, **kwargs) -> None: ...

def patch_keep_file_open_default(value) -> Generator[None, None, None]: ...
def test_keep_file_open_true_false_invalid() -> None: ...
def islock(l): ...
def test_pickle_lock() -> None: ...
def test_copy() -> None: ...
def test_copy_with_indexed_gzip_handle(tmp_path) -> None: ...

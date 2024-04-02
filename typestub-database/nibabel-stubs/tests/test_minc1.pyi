from _typeshed import Incomplete

from .. import Nifti1Image as Nifti1Image
from .. import load as load
from .. import minc1 as minc1
from ..deprecated import ModuleProxy as ModuleProxy
from ..deprecator import ExpiredDeprecationError as ExpiredDeprecationError
from ..externals.netcdf import netcdf_file as netcdf_file
from ..minc1 import Minc1File as Minc1File
from ..minc1 import Minc1Image as Minc1Image
from ..minc1 import MincHeader as MincHeader
from ..optpkg import optional_package as optional_package
from ..testing import assert_data_similar as assert_data_similar
from ..testing import clear_and_catch_warnings as clear_and_catch_warnings
from ..testing import data_path as data_path
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from . import test_spatialimages as tsi
from .test_fileslice import slicer_samples as slicer_samples

pyzstd: Incomplete
HAVE_ZSTD: Incomplete
_: Incomplete
EG_FNAME: Incomplete
EXAMPLE_IMAGES: Incomplete

class _TestMincFile:
    module = minc1
    file_class = Minc1File
    fname = EG_FNAME
    opener = netcdf_file
    test_files = EXAMPLE_IMAGES
    def test_mincfile(self) -> None: ...
    def test_mincfile_slicing(self) -> None: ...
    def test_load(self) -> None: ...
    def test_array_proxy_slicing(self) -> None: ...

class TestMinc1File(_TestMincFile):
    def test_compressed(self) -> None: ...

def test_header_data_io() -> None: ...

class TestMinc1Image(tsi.TestSpatialImage):
    image_class = Minc1Image
    eg_images: Incomplete
    module = minc1
    def test_data_to_from_fileobj(self) -> None: ...

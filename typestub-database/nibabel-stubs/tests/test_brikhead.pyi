from _typeshed import Incomplete

from .. import Nifti1Image as Nifti1Image
from .. import brikhead as brikhead
from .. import load as load
from ..testing import assert_data_similar as assert_data_similar
from ..testing import data_path as data_path
from .test_fileslice import slicer_samples as slicer_samples

EXAMPLE_IMAGES: Incomplete
EXAMPLE_BAD_IMAGES: Incomplete

class TestAFNIHeader:
    module = brikhead
    test_files = EXAMPLE_IMAGES
    def test_makehead(self) -> None: ...

class TestAFNIImage:
    module = brikhead
    test_files = EXAMPLE_IMAGES
    def test_brikheadfile(self) -> None: ...
    def test_load(self) -> None: ...
    def test_array_proxy_slicing(self) -> None: ...

class TestBadFiles:
    module = brikhead
    test_files = EXAMPLE_BAD_IMAGES
    def test_brikheadfile(self) -> None: ...

class TestBadVars:
    module = brikhead
    vars: Incomplete
    def test_unpack_var(self) -> None: ...

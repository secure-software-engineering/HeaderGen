from unittest import skipUnless as skipUnless

from _typeshed import Incomplete
from nibabel.affines import apply_affine as apply_affine
from nibabel.arrayproxy import ArrayProxy as ArrayProxy
from nibabel.fileslice import strided_scalar as strided_scalar
from nibabel.onetime import auto_attr as auto_attr
from nibabel.optpkg import optional_package as optional_package
from nibabel.spatialimages import SpatialImage as SpatialImage
from nibabel.tests.nibabel_data import get_nibabel_data as get_nibabel_data

h5: Incomplete
has_h5py: Incomplete
_: Incomplete
FS_DATA: Incomplete

class TestPointsets:
    rng: Incomplete
    def test_init(self, shape, homogeneous) -> None: ...
    def test_affines(self, shape, homogeneous) -> None: ...
    def test_homogeneous_coordinates(self) -> None: ...

def test_GridIndices() -> None: ...

class TestGrids(TestPointsets):
    def test_from_image(self, shape) -> None: ...
    def test_from_mask(self) -> None: ...
    def test_to_mask(self) -> None: ...

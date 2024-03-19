from _typeshed import Incomplete

from ..affines import from_matvec as from_matvec
from ..affines import to_matvec as to_matvec
from ..orientations import OrientationError as OrientationError
from ..orientations import aff2axcodes as aff2axcodes
from ..orientations import apply_orientation as apply_orientation
from ..orientations import axcodes2ornt as axcodes2ornt
from ..orientations import flip_axis as flip_axis
from ..orientations import inv_ornt_aff as inv_ornt_aff
from ..orientations import io_orientation as io_orientation
from ..orientations import ornt2axcodes as ornt2axcodes
from ..orientations import ornt_transform as ornt_transform
from ..testing import deprecated_to as deprecated_to
from ..testing import expires as expires

IN_ARRS: Incomplete
OUT_ORNTS: Incomplete
ALL_AXCODES: Incomplete
ALL_ORNTS: Incomplete

def same_transform(taff, ornt, shape): ...
def test_apply() -> None: ...
def test_io_orientation() -> None: ...
def test_ornt_transform() -> None: ...
def test_ornt2axcodes() -> None: ...
def test_axcodes2ornt() -> None: ...
def test_aff2axcodes() -> None: ...
def test_inv_ornt_aff() -> None: ...
def test_flip_axis_deprecation() -> None: ...

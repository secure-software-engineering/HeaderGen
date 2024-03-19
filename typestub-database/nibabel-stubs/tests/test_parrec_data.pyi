from _typeshed import Incomplete

from ..affines import voxel_sizes as voxel_sizes
from ..parrec import load as load
from .nibabel_data import get_nibabel_data as get_nibabel_data
from .nibabel_data import needs_nibabel_data as needs_nibabel_data

BALLS: Incomplete
OBLIQUE: Incomplete
AFF_OFF: Incomplete

def test_loading() -> None: ...
def test_fieldmap() -> None: ...
def test_oblique_loading() -> None: ...

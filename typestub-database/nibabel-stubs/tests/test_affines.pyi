from ..affines import AffineError as AffineError
from ..affines import append_diag as append_diag
from ..affines import apply_affine as apply_affine
from ..affines import dot_reduce as dot_reduce
from ..affines import from_matvec as from_matvec
from ..affines import obliquity as obliquity
from ..affines import rescale_affine as rescale_affine
from ..affines import to_matvec as to_matvec
from ..affines import voxel_sizes as voxel_sizes
from ..eulerangles import euler2mat as euler2mat
from ..orientations import aff2axcodes as aff2axcodes

def validated_apply_affine(T, xyz): ...
def test_apply_affine() -> None: ...
def test_matrix_vector() -> None: ...
def test_append_diag() -> None: ...
def test_dot_reduce() -> None: ...
def test_voxel_sizes() -> None: ...
def test_obliquity() -> None: ...
def test_rescale_affine() -> None: ...

from _typeshed import Incomplete

from .affines import AffineError as AffineError
from .affines import append_diag as append_diag
from .affines import from_matvec as from_matvec
from .affines import rescale_affine as rescale_affine
from .affines import to_matvec as to_matvec
from .imageclasses import spatial_axes_first as spatial_axes_first
from .nifti1 import Nifti1Image as Nifti1Image
from .optpkg import optional_package as optional_package
from .orientations import axcodes2ornt as axcodes2ornt
from .orientations import io_orientation as io_orientation
from .orientations import ornt_transform as ornt_transform
from .spaces import vox2out_vox as vox2out_vox

spnd: Incomplete
SIGMA2FWHM: Incomplete

def fwhm2sigma(fwhm): ...
def sigma2fwhm(sigma): ...
def adapt_affine(affine, n_dim): ...
def resample_from_to(
    from_img,
    to_vox_map,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    out_class=...,
): ...
def resample_to_output(
    in_img,
    voxel_sizes: Incomplete | None = None,
    order: int = 3,
    mode: str = "constant",
    cval: float = 0.0,
    out_class=...,
): ...
def smooth_image(
    img, fwhm, mode: str = "nearest", cval: float = 0.0, out_class=...
): ...
def conform(
    from_img,
    out_shape=(256, 256, 256),
    voxel_size=(1.0, 1.0, 1.0),
    order: int = 3,
    cval: float = 0.0,
    orientation: str = "RAS",
    out_class: Incomplete | None = None,
): ...

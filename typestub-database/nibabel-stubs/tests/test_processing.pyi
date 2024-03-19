from _typeshed import Incomplete
from nibabel.affines import AffineError as AffineError
from nibabel.affines import apply_affine as apply_affine
from nibabel.affines import from_matvec as from_matvec
from nibabel.affines import to_matvec as to_matvec
from nibabel.affines import voxel_sizes as voxel_sizes
from nibabel.eulerangles import euler2mat as euler2mat
from nibabel.nifti1 import Nifti1Image as Nifti1Image
from nibabel.nifti2 import Nifti2Image as Nifti2Image
from nibabel.optpkg import optional_package as optional_package
from nibabel.orientations import aff2axcodes as aff2axcodes
from nibabel.orientations import inv_ornt_aff as inv_ornt_aff
from nibabel.processing import adapt_affine as adapt_affine
from nibabel.processing import conform as conform
from nibabel.processing import fwhm2sigma as fwhm2sigma
from nibabel.processing import resample_from_to as resample_from_to
from nibabel.processing import resample_to_output as resample_to_output
from nibabel.processing import sigma2fwhm as sigma2fwhm
from nibabel.processing import smooth_image as smooth_image
from nibabel.testing import assert_allclose_safely as assert_allclose_safely
from nibabel.tests.test_spaces import assert_all_in as assert_all_in
from nibabel.tests.test_spaces import get_outspace_params as get_outspace_params

from .test_imageclasses import MINC_3DS as MINC_3DS
from .test_imageclasses import MINC_4DS as MINC_4DS

spnd: Incomplete
have_scipy: Incomplete
_: Incomplete
needs_scipy: Incomplete
DATA_DIR: Incomplete
OTHER_IMGS: Incomplete

def test_sigma2fwhm() -> None: ...
def test_adapt_affine() -> None: ...
def test_resample_from_to(caplog) -> None: ...
def test_resample_to_output(caplog) -> None: ...
def test_smooth_image(caplog) -> None: ...
def test_spatial_axes_check(caplog) -> None: ...
def assert_spm_resampling_close(from_img, our_resampled, spm_resampled) -> None: ...
def test_against_spm_resample() -> None: ...
def test_conform(caplog) -> None: ...

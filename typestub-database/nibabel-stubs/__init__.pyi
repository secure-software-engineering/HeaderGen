from _typeshed import Incomplete

from . import ecat as ecat
from . import imagestats as imagestats
from . import mriutils as mriutils
from . import orientations as orientations
from . import streamlines as streamlines
from . import viewers as viewers
from .analyze import AnalyzeHeader as AnalyzeHeader
from .analyze import AnalyzeImage as AnalyzeImage
from .arrayproxy import is_proxy as is_proxy
from .cifti2 import Cifti2Header as Cifti2Header
from .cifti2 import Cifti2Image as Cifti2Image
from .fileholders import FileHolder as FileHolder
from .fileholders import FileHolderError as FileHolderError
from .freesurfer import MGHImage as MGHImage
from .funcs import as_closest_canonical as as_closest_canonical
from .funcs import concat_images as concat_images
from .funcs import four_to_three as four_to_three
from .funcs import squeeze_image as squeeze_image
from .gifti import GiftiImage as GiftiImage
from .imageclasses import all_image_classes as all_image_classes
from .loadsave import load as load
from .loadsave import save as save
from .minc1 import Minc1Image as Minc1Image
from .minc2 import Minc2Image as Minc2Image
from .nifti1 import Nifti1Header as Nifti1Header
from .nifti1 import Nifti1Image as Nifti1Image
from .nifti1 import Nifti1Pair as Nifti1Pair
from .nifti2 import Nifti2Header as Nifti2Header
from .nifti2 import Nifti2Image as Nifti2Image
from .nifti2 import Nifti2Pair as Nifti2Pair
from .orientations import OrientationError as OrientationError
from .orientations import aff2axcodes as aff2axcodes
from .orientations import apply_orientation as apply_orientation
from .orientations import flip_axis as flip_axis
from .orientations import io_orientation as io_orientation
from .pkg_info import __version__ as __version__
from .spm2analyze import Spm2AnalyzeHeader as Spm2AnalyzeHeader
from .spm2analyze import Spm2AnalyzeImage as Spm2AnalyzeImage
from .spm99analyze import Spm99AnalyzeHeader as Spm99AnalyzeHeader
from .spm99analyze import Spm99AnalyzeImage as Spm99AnalyzeImage

def get_info(): ...
def test(
    label: Incomplete | None = None,
    verbose: int = 1,
    extra_argv: Incomplete | None = None,
    doctests: bool = False,
    coverage: bool = False,
    raise_warnings: Incomplete | None = None,
    timer: bool = False,
): ...
def bench(
    label: Incomplete | None = None,
    verbose: int = 1,
    extra_argv: Incomplete | None = None,
): ...

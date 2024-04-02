from .analyze import AnalyzeImage as AnalyzeImage
from .brikhead import AFNIImage as AFNIImage
from .cifti2 import Cifti2Image as Cifti2Image
from .dataobj_images import DataobjImage as DataobjImage
from .filebasedimages import FileBasedImage as FileBasedImage
from .freesurfer import MGHImage as MGHImage
from .gifti import GiftiImage as GiftiImage
from .minc1 import Minc1Image as Minc1Image
from .minc2 import Minc2Image as Minc2Image
from .nifti1 import Nifti1Image as Nifti1Image
from .nifti1 import Nifti1Pair as Nifti1Pair
from .nifti2 import Nifti2Image as Nifti2Image
from .nifti2 import Nifti2Pair as Nifti2Pair
from .parrec import PARRECImage as PARRECImage
from .spm2analyze import Spm2AnalyzeImage as Spm2AnalyzeImage
from .spm99analyze import Spm99AnalyzeImage as Spm99AnalyzeImage

all_image_classes: list[type[FileBasedImage]]
KNOWN_SPATIAL_FIRST: tuple[type[FileBasedImage], ...]

def spatial_axes_first(img: DataobjImage) -> bool: ...

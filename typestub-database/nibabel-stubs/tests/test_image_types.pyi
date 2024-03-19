from _typeshed import Incomplete

from .. import MGHImage as MGHImage
from .. import Minc1Image as Minc1Image
from .. import Minc2Image as Minc2Image
from .. import Nifti1Image as Nifti1Image
from .. import Nifti1Pair as Nifti1Pair
from .. import Nifti2Image as Nifti2Image
from .. import Nifti2Pair as Nifti2Pair
from .. import Spm2AnalyzeImage as Spm2AnalyzeImage
from .. import all_image_classes as all_image_classes

DATA_PATH: Incomplete

def test_sniff_and_guessed_image_type(img_klasses=...): ...
def test_sniff_and_guessed_image_type_randomized() -> None: ...

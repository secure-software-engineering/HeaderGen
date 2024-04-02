from _typeshed import Incomplete

from .. import Nifti1Image as Nifti1Image
from .dicomwrappers import wrapper_from_data as wrapper_from_data
from .dicomwrappers import wrapper_from_file as wrapper_from_file

class DicomReadError(Exception): ...

DPCS_TO_TAL: Incomplete

def mosaic_to_nii(dcm_data): ...
def read_mosaic_dwi_dir(
    dicom_path, globber: str = "*.dcm", dicom_kwargs: Incomplete | None = None
): ...
def read_mosaic_dir(
    dicom_path,
    globber: str = "*.dcm",
    check_is_dwi: bool = False,
    dicom_kwargs: Incomplete | None = None,
): ...
def slices_to_series(wrappers): ...

from collections.abc import Generator

from _typeshed import Incomplete
from nibabel.optpkg import optional_package as optional_package

from .nifti1 import Nifti1Header as Nifti1Header

pydicom: Incomplete
logger: Incomplete

class DFTError(Exception): ...
class CachingError(DFTError): ...
class VolumeError(DFTError): ...

class InstanceStackError(DFTError):
    series: Incomplete
    i: Incomplete
    si: Incomplete
    def __init__(self, series, i, si) -> None: ...

class _Study:
    uid: Incomplete
    date: Incomplete
    time: Incomplete
    comments: Incomplete
    patient_name: Incomplete
    patient_id: Incomplete
    patient_birth_date: Incomplete
    patient_sex: Incomplete
    series: Incomplete
    def __init__(self, d) -> None: ...
    def __getattribute__(self, name): ...
    def patient_name_or_uid(self): ...

class _Series:
    uid: Incomplete
    study: Incomplete
    number: Incomplete
    description: Incomplete
    rows: Incomplete
    columns: Incomplete
    bits_allocated: Incomplete
    bits_stored: Incomplete
    storage_instances: Incomplete
    def __init__(self, d) -> None: ...
    def __getattribute__(self, name): ...
    def as_png(self, index: Incomplete | None = None, scale_to_slice: bool = True): ...
    def png_size(
        self, index: Incomplete | None = None, scale_to_slice: bool = True
    ): ...
    def as_nifti(self): ...
    def nifti_size(self): ...

class _StorageInstance:
    uid: Incomplete
    instance_number: Incomplete
    series: Incomplete
    files: Incomplete
    def __init__(self, d) -> None: ...
    def __getattribute__(self, name): ...
    def dicom(self): ...

def update_cache(base_dir, followlinks: bool = False) -> None: ...
def get_studies(base_dir: Incomplete | None = None, followlinks: bool = False): ...
def clear_cache() -> None: ...

CREATE_QUERIES: Incomplete

class _DB:
    fname: Incomplete
    verbose: Incomplete
    def __init__(
        self, fname: Incomplete | None = None, verbose: bool = True
    ) -> None: ...
    @property
    def session(self): ...
    def readonly_cursor(self) -> Generator[Incomplete, None, None]: ...
    def readwrite_cursor(self) -> Generator[Incomplete, None, None]: ...

DB: Incomplete

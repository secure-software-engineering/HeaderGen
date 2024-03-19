from typing import Callable

from _typeshed import Incomplete

from .deprecated import deprecate_with_version as deprecate_with_version
from .optpkg import optional_package as optional_package

pydicom: Incomplete
have_dicom: Incomplete
_: Incomplete
read_file: Callable | None
tag_for_keyword: Callable | None
Sequence: type | None

def dicom_test(func): ...

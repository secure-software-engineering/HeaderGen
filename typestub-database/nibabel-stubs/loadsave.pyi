import typing as ty

from .arrayproxy import is_proxy as is_proxy
from .deprecated import deprecate_with_version as deprecate_with_version
from .filebasedimages import FileBasedImage as FileBasedImage
from .filebasedimages import ImageFileError as ImageFileError
from .filename_parser import FileSpec as FileSpec
from .filename_parser import splitext_addext as splitext_addext
from .imageclasses import all_image_classes as all_image_classes
from .openers import ImageOpener as ImageOpener

P = ty.ParamSpec("P")

class Signature(ty.TypedDict):
    signature: bytes
    format_name: str

def load(filename: FileSpec, **kwargs) -> FileBasedImage: ...
def guessed_image_type(filename): ...
def save(img: FileBasedImage, filename: FileSpec, **kwargs) -> None: ...
def read_img_data(img, prefer: str = "scaled"): ...

from collections.abc import Generator

from _typeshed import Incomplete

from ..filebasedimages import FileBasedHeader as FileBasedHeader
from ..filebasedimages import FileBasedImage as FileBasedImage
from ..filebasedimages import SerializableImage as SerializableImage
from .test_image_api import GenericImageAPI as GenericImageAPI
from .test_image_api import SerializeMixin as SerializeMixin

class FBNumpyImage(FileBasedImage):
    header_class = FileBasedHeader
    valid_exts: Incomplete
    files_types: Incomplete
    arr: Incomplete
    def __init__(
        self,
        arr,
        header: Incomplete | None = None,
        extra: Incomplete | None = None,
        file_map: Incomplete | None = None,
    ) -> None: ...
    @property
    def shape(self): ...
    def get_data(self): ...
    @property
    def dataobj(self): ...
    def get_fdata(self): ...
    @classmethod
    def from_file_map(klass, file_map): ...
    def to_file_map(self, file_map: Incomplete | None = None) -> None: ...
    def get_data_dtype(self): ...
    def set_data_dtype(self, dtype) -> None: ...

class SerializableNumpyImage(FBNumpyImage, SerializableImage): ...

class TestFBImageAPI(GenericImageAPI):
    image_maker = FBNumpyImage
    header_maker = FileBasedHeader
    example_shapes: Incomplete
    example_dtypes: Incomplete
    can_save: bool
    standard_extension: str
    def make_imaker(self, arr, header: Incomplete | None = None): ...
    def obj_params(self) -> Generator[Incomplete, None, None]: ...

class TestSerializableImageAPI(TestFBImageAPI, SerializeMixin):
    image_maker = SerializableNumpyImage

def test_filebased_header() -> None: ...

class MultipartNumpyImage(FBNumpyImage):
    files_types: Incomplete

class SerializableMPNumpyImage(MultipartNumpyImage, SerializableImage): ...

def test_multifile_stream_failure() -> None: ...

from _typeshed import Incomplete
from nibabel.dataobj_images import DataobjImage as DataobjImage
from nibabel.filebasedimages import FileBasedHeader as FileBasedHeader
from nibabel.tests.test_filebasedimages import TestFBImageAPI as _TFI
from nibabel.tests.test_image_api import DataInterfaceMixin as DataInterfaceMixin

class DoNumpyImage(DataobjImage):
    header_class = FileBasedHeader
    valid_exts: Incomplete
    files_types: Incomplete
    @classmethod
    def from_file_map(
        klass, file_map, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...
    def to_file_map(self, file_map: Incomplete | None = None) -> None: ...
    def get_data_dtype(self): ...
    def set_data_dtype(self, dtype) -> None: ...

class TestDataobjAPI(_TFI, DataInterfaceMixin):
    image_maker = DoNumpyImage

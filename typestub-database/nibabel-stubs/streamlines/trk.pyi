from _typeshed import Incomplete
from nibabel.openers import Opener as Opener
from nibabel.orientations import aff2axcodes as aff2axcodes
from nibabel.orientations import axcodes2ornt as axcodes2ornt
from nibabel.volumeutils import endian_codes as endian_codes
from nibabel.volumeutils import native_code as native_code
from nibabel.volumeutils import swapped_code as swapped_code

from .array_sequence import (
    create_arraysequences_from_generator as create_arraysequences_from_generator,
)
from .header import Field as Field
from .tractogram import LazyTractogram as LazyTractogram
from .tractogram import Tractogram as Tractogram
from .tractogram import TractogramItem as TractogramItem
from .tractogram_file import DataError as DataError
from .tractogram_file import HeaderError as HeaderError
from .tractogram_file import HeaderWarning as HeaderWarning
from .tractogram_file import TractogramFile as TractogramFile
from .utils import peek_next as peek_next

MAX_NB_NAMED_SCALARS_PER_POINT: int
MAX_NB_NAMED_PROPERTIES_PER_STREAMLINE: int
header_2_dtd: Incomplete
header_2_dtype: Incomplete

def get_affine_trackvis_to_rasmm(header): ...
def get_affine_rasmm_to_trackvis(header): ...
def encode_value_in_name(value, name, max_name_len: int = 20): ...
def decode_value_from_name(encoded_name): ...

class TrkFile(TractogramFile):
    MAGIC_NUMBER: bytes
    HEADER_SIZE: int
    SUPPORTS_DATA_PER_POINT: bool
    SUPPORTS_DATA_PER_STREAMLINE: bool
    def __init__(self, tractogram, header: Incomplete | None = None) -> None: ...
    @classmethod
    def is_correct_format(cls, fileobj): ...
    @classmethod
    def create_empty_header(cls, endianness: Incomplete | None = None): ...
    @classmethod
    def load(cls, fileobj, lazy_load: bool = False): ...
    def save(self, fileobj) -> None: ...

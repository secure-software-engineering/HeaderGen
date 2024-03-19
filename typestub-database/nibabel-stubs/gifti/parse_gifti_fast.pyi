from xml.parsers.expat import ExpatError

from _typeshed import Incomplete

from ..nifti1 import data_type_codes as data_type_codes
from ..nifti1 import intent_codes as intent_codes
from ..nifti1 import xform_codes as xform_codes
from ..xmlutils import XmlParser as XmlParser
from .gifti import GiftiCoordSystem as GiftiCoordSystem
from .gifti import GiftiDataArray as GiftiDataArray
from .gifti import GiftiImage as GiftiImage
from .gifti import GiftiLabel as GiftiLabel
from .gifti import GiftiLabelTable as GiftiLabelTable
from .gifti import GiftiMetaData as GiftiMetaData
from .util import array_index_order_codes as array_index_order_codes
from .util import gifti_encoding_codes as gifti_encoding_codes
from .util import gifti_endian_codes as gifti_endian_codes

class GiftiParseError(ExpatError): ...

def read_data_block(darray, fname, data, mmap): ...

class GiftiImageParser(XmlParser):
    img: Incomplete
    mmap: Incomplete
    fsm_state: Incomplete
    nvpair: Incomplete
    da: Incomplete
    coordsys: Incomplete
    lata: Incomplete
    label: Incomplete
    meta_global: Incomplete
    meta_da: Incomplete
    count_da: bool
    write_to: Incomplete
    def __init__(
        self,
        encoding: Incomplete | None = None,
        buffer_size: int = 35000000,
        verbose: int = 0,
        mmap: bool = True,
    ) -> None: ...
    expected_numDA: Incomplete
    def StartElementHandler(self, name, attrs) -> None: ...
    def EndElementHandler(self, name) -> None: ...
    def CharacterDataHandler(self, data) -> None: ...
    endian: Incomplete
    def flush_chardata(self) -> None: ...
    @property
    def pending_data(self): ...

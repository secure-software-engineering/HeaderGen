from typing import Type

from _typeshed import Incomplete

from .. import xmlutils as xml
from ..caret import CaretMetaData as CaretMetaData
from ..deprecated import deprecate_with_version as deprecate_with_version
from ..filebasedimages import SerializableImage as SerializableImage
from ..nifti1 import data_type_codes as data_type_codes
from ..nifti1 import intent_codes as intent_codes
from ..nifti1 import xform_codes as xform_codes
from .parse_gifti_fast import GiftiImageParser as GiftiImageParser
from .util import KIND2FMT as KIND2FMT
from .util import array_index_order_codes as array_index_order_codes
from .util import gifti_encoding_codes as gifti_encoding_codes
from .util import gifti_endian_codes as gifti_endian_codes

GIFTI_DTYPES: Incomplete

class _GiftiMDList(list):
    def __init__(self, metadata) -> None: ...
    def append(self, nvpair) -> None: ...
    def clear(self) -> None: ...
    def extend(self, iterable) -> None: ...
    def insert(self, index, nvpair) -> None: ...
    def pop(self, index: int = -1): ...
    def remove(self, nvpair) -> None: ...

class GiftiMetaData(CaretMetaData):
    @property
    def data(self): ...
    @classmethod
    def from_dict(klass, data_dict): ...
    @property
    def metadata(self): ...
    def print_summary(self) -> None: ...

class GiftiNVPairs:
    def __init__(self, name: str = "", value: str = "") -> None: ...
    def __eq__(self, other): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, key) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, val) -> None: ...

class GiftiLabelTable(xml.XmlSerializable):
    labels: Incomplete
    def __init__(self) -> None: ...
    labels_as_dict: Incomplete
    def get_labels_as_dict(self): ...
    def print_summary(self) -> None: ...

class GiftiLabel(xml.XmlSerializable):
    key: Incomplete
    red: Incomplete
    green: Incomplete
    blue: Incomplete
    alpha: Incomplete
    def __init__(
        self,
        key: int = 0,
        red: Incomplete | None = None,
        green: Incomplete | None = None,
        blue: Incomplete | None = None,
        alpha: Incomplete | None = None,
    ) -> None: ...
    @property
    def rgba(self): ...
    @rgba.setter
    def rgba(self, rgba) -> None: ...

class GiftiCoordSystem(xml.XmlSerializable):
    dataspace: Incomplete
    xformspace: Incomplete
    xform: Incomplete
    def __init__(
        self, dataspace: int = 0, xformspace: int = 0, xform: Incomplete | None = None
    ) -> None: ...
    def print_summary(self) -> None: ...

class GiftiDataArray(xml.XmlSerializable):
    data: Incomplete
    intent: Incomplete
    datatype: Incomplete
    encoding: Incomplete
    endian: Incomplete
    coordsys: Incomplete
    ind_ord: Incomplete
    meta: Incomplete
    ext_fname: Incomplete
    ext_offset: Incomplete
    dims: Incomplete
    def __init__(
        self,
        data: Incomplete | None = None,
        intent: str = "NIFTI_INTENT_NONE",
        datatype: Incomplete | None = None,
        encoding: str = "GIFTI_ENCODING_B64GZ",
        endian=...,
        coordsys: Incomplete | None = None,
        ordering: str = "C",
        meta: Incomplete | None = None,
        ext_fname: str = "",
        ext_offset: int = 0,
    ) -> None: ...
    @property
    def num_dim(self): ...
    def print_summary(self) -> None: ...
    @property
    def metadata(self): ...

class GiftiImage(xml.XmlSerializable, SerializableImage):
    valid_exts: Incomplete
    files_types: Incomplete
    parser: Type[xml.XmlParser]
    darrays: Incomplete
    version: Incomplete
    def __init__(
        self,
        header: Incomplete | None = None,
        extra: Incomplete | None = None,
        file_map: Incomplete | None = None,
        meta: Incomplete | None = None,
        labeltable: Incomplete | None = None,
        darrays: Incomplete | None = None,
        version: str = "1.0",
    ) -> None: ...
    @property
    def numDA(self): ...
    @property
    def labeltable(self): ...
    @labeltable.setter
    def labeltable(self, labeltable) -> None: ...
    @property
    def meta(self): ...
    @meta.setter
    def meta(self, meta) -> None: ...
    def add_gifti_data_array(self, dataarr) -> None: ...
    def remove_gifti_data_array(self, ith) -> None: ...
    def remove_gifti_data_array_by_intent(self, intent) -> None: ...
    def get_arrays_from_intent(self, intent): ...
    def agg_data(self, intent_code: Incomplete | None = None): ...
    def print_summary(self) -> None: ...
    def to_xml(
        self, enc: str = "utf-8", *, mode: str = "strict", **kwargs
    ) -> bytes: ...
    def to_bytes(self, enc: str = "utf-8", *, mode: str = "strict"): ...
    def to_file_map(
        self,
        file_map: Incomplete | None = None,
        enc: str = "utf-8",
        *,
        mode: str = "strict"
    ) -> None: ...
    @classmethod
    def from_file_map(
        klass, file_map, buffer_size: int = 35000000, mmap: bool = True
    ): ...
    @classmethod
    def from_filename(
        klass, filename, buffer_size: int = 35000000, mmap: bool = True
    ): ...

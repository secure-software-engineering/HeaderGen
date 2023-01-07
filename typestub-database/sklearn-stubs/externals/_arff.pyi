from typing import Any, Iterator, List, Optional, Tuple, Union
from typing_extensions import TypedDict

__author_email__: str
ArffDenseDataType = Iterator[List]
ArffSparseDataType = Tuple[List, ...]

class ArffContainerType(TypedDict):
    description: str
    relation: str
    attributes: List
    data: Union[ArffDenseDataType, ArffSparseDataType]

DENSE: int
COO: int
LOD: int
DENSE_GEN: int
LOD_GEN: int

class ArffException(Exception):
    message: Optional[str]
    line: int
    def __init__(self) -> None: ...

class BadRelationFormat(ArffException):
    message: str

class BadAttributeFormat(ArffException):
    message: str

class BadDataFormat(ArffException):
    message: Any
    def __init__(self, value) -> None: ...

class BadAttributeType(ArffException):
    message: str

class BadAttributeName(ArffException):
    message: Any
    def __init__(self, value, value2) -> None: ...

class BadNominalValue(ArffException):
    message: Any
    def __init__(self, value) -> None: ...

class BadNominalFormatting(ArffException):
    message: Any
    def __init__(self, value) -> None: ...

class BadNumericalValue(ArffException):
    message: str

class BadStringValue(ArffException):
    message: str

class BadLayout(ArffException):
    message: str
    def __init__(self, msg: str = ...) -> None: ...

class BadObject(ArffException):
    msg: Any
    def __init__(self, msg: str = ...) -> None: ...

def encode_string(s): ...

class EncodedNominalConversor:
    values: Any
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class NominalConversor:
    values: Any
    zero_value: Any
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class DenseGeneratorData:
    def decode_rows(self, stream, conversors) -> None: ...
    def encode_data(self, data, attributes) -> None: ...

class _DataListMixin:
    def decode_rows(self, stream, conversors): ...

class Data(_DataListMixin, DenseGeneratorData): ...

class COOData:
    def decode_rows(self, stream, conversors): ...
    def encode_data(self, data, attributes) -> None: ...

class LODGeneratorData:
    def decode_rows(self, stream, conversors) -> None: ...
    def encode_data(self, data, attributes) -> None: ...

class LODData(_DataListMixin, LODGeneratorData): ...

class ArffDecoder:
    def __init__(self) -> None: ...
    def decode(self, s, encode_nominal: bool = ..., return_type=...): ...

class ArffEncoder:
    def encode(self, obj): ...
    def iter_encode(self, obj) -> None: ...

def load(fp, encode_nominal: bool = ..., return_type=...): ...
def loads(s, encode_nominal: bool = ..., return_type=...): ...
def dump(obj, fp): ...
def dumps(obj): ...

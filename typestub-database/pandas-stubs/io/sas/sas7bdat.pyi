import numpy as np
from collections import abc
from pandas import DataFrame as DataFrame, isna as isna
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.errors import EmptyDataError as EmptyDataError, OutOfBoundsDatetime as OutOfBoundsDatetime
from pandas.io.common import get_handle as get_handle
from pandas.io.sas._sas import Parser as Parser
from pandas.io.sas.sasreader import ReaderBase as ReaderBase
from typing import Union, Any

class _SubheaderPointer:
    offset: int
    length: int
    compression: int
    ptype: int
    def __init__(self, offset: int, length: int, compression: int, ptype: int) -> None: ...

class _Column:
    col_id: int
    name: Union[str, bytes]
    label: Union[str, bytes]
    format: Union[str, bytes]
    ctype: bytes
    length: int
    def __init__(self, col_id: int, name: Union[str, bytes], label: Union[str, bytes], format: Union[str, bytes], ctype: bytes, length: int) -> None: ...

class SAS7BDATReader(ReaderBase, abc.Iterator):
    index: Any
    convert_dates: Any
    blank_missing: Any
    chunksize: Any
    encoding: Any
    convert_text: Any
    convert_header_text: Any
    default_encoding: str
    compression: bytes
    column_names_strings: Any
    column_names: Any
    column_formats: Any
    columns: Any
    handles: Any
    def __init__(self, path_or_buf: Union[FilePath, ReadBuffer[bytes]], index: Any | None = ..., convert_dates: bool = ..., blank_missing: bool = ..., chunksize: Any | None = ..., encoding: Any | None = ..., convert_text: bool = ..., convert_header_text: bool = ...) -> None: ...
    def column_data_lengths(self) -> np.ndarray: ...
    def column_data_offsets(self) -> np.ndarray: ...
    def column_types(self) -> np.ndarray: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def read(self, nrows: Union[int, None] = ...) -> Union[DataFrame, None]: ...

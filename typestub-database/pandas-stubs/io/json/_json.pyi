import abc
from abc import ABC, abstractmethod
from typing import Any, Callable, Mapping, Union

from pandas import MultiIndex as MultiIndex
from pandas import Series as Series
from pandas import isna as isna
from pandas import notna as notna
from pandas import to_datetime as to_datetime
from pandas._libs.tslibs import iNaT as iNaT
from pandas._typing import CompressionOptions as CompressionOptions
from pandas._typing import DtypeArg as DtypeArg
from pandas._typing import IndexLabel as IndexLabel
from pandas._typing import JSONSerializable as JSONSerializable
from pandas._typing import StorageOptions as StorageOptions
from pandas.core.construction import (
    create_series_with_explicit_dtype as create_series_with_explicit_dtype,
)
from pandas.core.dtypes.common import ensure_str as ensure_str
from pandas.core.dtypes.common import is_period_dtype as is_period_dtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.reshape.concat import concat as concat
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import IOHandles as IOHandles
from pandas.io.common import file_exists as file_exists
from pandas.io.common import get_handle as get_handle
from pandas.io.common import is_fsspec_url as is_fsspec_url
from pandas.io.common import is_url as is_url
from pandas.io.common import stringify_path as stringify_path
from pandas.io.json._normalize import (
    convert_to_line_delimits as convert_to_line_delimits,
)
from pandas.io.json._table_schema import build_table_schema as build_table_schema
from pandas.io.json._table_schema import parse_table_schema as parse_table_schema
from pandas.io.parsers.readers import validate_integer as validate_integer
from pandas.util._decorators import deprecate_kwarg as deprecate_kwarg
from pandas.util._decorators import (
    deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments,
)
from pandas.util._decorators import doc as doc

loads: Any
dumps: Any

def to_json(
    path_or_buf,
    obj: NDFrame,
    orient: Union[str, None] = ...,
    date_format: str = ...,
    double_precision: int = ...,
    force_ascii: bool = ...,
    date_unit: str = ...,
    default_handler: Union[Callable[[Any], JSONSerializable], None] = ...,
    lines: bool = ...,
    compression: CompressionOptions = ...,
    index: bool = ...,
    indent: int = ...,
    storage_options: StorageOptions = ...,
): ...

class Writer(ABC, metaclass=abc.ABCMeta):
    obj: Any
    orient: Any
    date_format: Any
    double_precision: Any
    ensure_ascii: Any
    date_unit: Any
    default_handler: Any
    index: Any
    indent: Any
    is_copy: Any
    def __init__(
        self,
        obj,
        orient: Union[str, None],
        date_format: str,
        double_precision: int,
        ensure_ascii: bool,
        date_unit: str,
        index: bool,
        default_handler: Union[Callable[[Any], JSONSerializable], None] = ...,
        indent: int = ...,
    ) -> None: ...
    def write(self): ...
    @property
    @abstractmethod
    def obj_to_write(self) -> Union[NDFrame, Mapping[IndexLabel, Any]]: ...

class SeriesWriter(Writer):
    @property
    def obj_to_write(self) -> Union[NDFrame, Mapping[IndexLabel, Any]]: ...

class FrameWriter(Writer):
    @property
    def obj_to_write(self) -> Union[NDFrame, Mapping[IndexLabel, Any]]: ...

class JSONTableWriter(FrameWriter):
    schema: Any
    obj: Any
    date_format: str
    orient: str
    index: Any
    def __init__(
        self,
        obj,
        orient: Union[str, None],
        date_format: str,
        double_precision: int,
        ensure_ascii: bool,
        date_unit: str,
        index: bool,
        default_handler: Union[Callable[[Any], JSONSerializable], None] = ...,
        indent: int = ...,
    ): ...
    @property
    def obj_to_write(self) -> Union[NDFrame, Mapping[IndexLabel, Any]]: ...

def read_json(
    path_or_buf: Any | None = ...,
    orient: Any | None = ...,
    typ: str = ...,
    dtype: Union[DtypeArg, None] = ...,
    convert_axes: Any | None = ...,
    convert_dates: bool = ...,
    keep_default_dates: bool = ...,
    numpy: bool = ...,
    precise_float: bool = ...,
    date_unit: Any | None = ...,
    encoding: Any | None = ...,
    encoding_errors: Union[str, None] = ...,
    lines: bool = ...,
    chunksize: Union[int, None] = ...,
    compression: CompressionOptions = ...,
    nrows: Union[int, None] = ...,
    storage_options: StorageOptions = ...,
) -> DataFrame: ...

class JsonReader(abc.Iterator):
    orient: Any
    typ: Any
    dtype: Any
    convert_axes: Any
    convert_dates: Any
    keep_default_dates: Any
    numpy: Any
    precise_float: Any
    date_unit: Any
    encoding: Any
    compression: Any
    storage_options: Any
    lines: Any
    chunksize: Any
    nrows_seen: int
    nrows: Any
    encoding_errors: Any
    handles: Any
    data: Any
    def __init__(
        self,
        filepath_or_buffer,
        orient,
        typ,
        dtype,
        convert_axes,
        convert_dates,
        keep_default_dates: bool,
        numpy: bool,
        precise_float: bool,
        date_unit,
        encoding,
        lines: bool,
        chunksize: Union[int, None],
        compression: CompressionOptions,
        nrows: Union[int, None],
        storage_options: StorageOptions = ...,
        encoding_errors: Union[str, None] = ...,
    ) -> None: ...
    def read(self): ...
    def close(self) -> None: ...
    def __next__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Parser:
    json: Any
    orient: Any
    dtype: Any
    min_stamp: Any
    numpy: Any
    precise_float: Any
    convert_axes: Any
    convert_dates: Any
    date_unit: Any
    keep_default_dates: Any
    obj: Any
    def __init__(
        self,
        json,
        orient,
        dtype: Union[DtypeArg, None] = ...,
        convert_axes: bool = ...,
        convert_dates: bool = ...,
        keep_default_dates: bool = ...,
        numpy: bool = ...,
        precise_float: bool = ...,
        date_unit: Any | None = ...,
    ) -> None: ...
    def check_keys_split(self, decoded) -> None: ...
    def parse(self): ...

class SeriesParser(Parser): ...
class FrameParser(Parser): ...

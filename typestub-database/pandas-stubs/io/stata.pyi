import datetime
import numpy as np
from collections import abc
from pandas import Categorical as Categorical, DatetimeIndex as DatetimeIndex, NaT as NaT, Timestamp as Timestamp, isna as isna, to_datetime as to_datetime, to_timedelta as to_timedelta
from pandas._libs.lib import infer_dtype as infer_dtype
from pandas._libs.writers import max_len_string_array as max_len_string_array
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.arrays.boolean import BooleanDtype as BooleanDtype
from pandas.core.dtypes.common import ensure_object as ensure_object, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_numeric_dtype as is_numeric_dtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.base import Index as Index
from pandas.core.series import Series as Series
from pandas.io.common import get_handle as get_handle
from pandas.util._decorators import Appender as Appender, doc as doc
from typing import Union, Any, Hashable, Literal, Sequence

stata_epoch: Any
excessive_string_length_error: str

class PossiblePrecisionLoss(Warning): ...

precision_loss_doc: str

class ValueLabelTypeMismatch(Warning): ...

value_label_mismatch_doc: str

class InvalidColumnName(Warning): ...

invalid_name_doc: str

class CategoricalConversionWarning(Warning): ...

categorical_conversion_warning: str

class StataValueLabel:
    labname: Any
    value_labels: Any
    def __init__(self, catarray: Series, encoding: str = ...): ...
    def generate_value_label(self, byteorder: str) -> bytes: ...

class StataNonCatValueLabel(StataValueLabel):
    labname: Any
    value_labels: Any
    def __init__(self, labname: str, value_labels: dict[Union[float, int], str], encoding: Literal['latin-1', 'utf-8'] = ...): ...

class StataMissingValue:
    MISSING_VALUES: dict[float, str]
    bases: Any
    float32_base: bytes
    increment: Any
    key: Any
    int_value: Any
    float64_base: bytes
    BASE_MISSING_VALUES: Any
    def __init__(self, value: Union[int, float]) -> None: ...
    @property
    def string(self) -> str: ...
    @property
    def value(self) -> Union[int, float]: ...
    def __eq__(self, other: Any) -> bool: ...
    @classmethod
    def get_base_missing_value(cls, dtype: np.dtype) -> Union[int, float]: ...

class StataParser:
    DTYPE_MAP: Any
    DTYPE_MAP_XML: Any
    TYPE_MAP: Any
    TYPE_MAP_XML: Any
    VALID_RANGE: Any
    OLD_TYPE_MAPPING: Any
    MISSING_VALUES: Any
    NUMPY_TYPE_MAP: Any
    RESERVED_WORDS: Any
    def __init__(self) -> None: ...

class StataReader(StataParser, abc.Iterator):
    __doc__: Any
    col_sizes: Any
    path_or_buf: Any
    def __init__(self, path_or_buf: Union[FilePath, ReadBuffer[bytes]], convert_dates: bool = ..., convert_categoricals: bool = ..., index_col: Union[str, None] = ..., convert_missing: bool = ..., preserve_dtypes: bool = ..., columns: Union[Sequence[str], None] = ..., order_categoricals: bool = ..., chunksize: Union[int, None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ...) -> None: ...
    def __enter__(self) -> StataReader: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def get_chunk(self, size: Union[int, None] = ...) -> DataFrame: ...
    def read(self, nrows: Union[int, None] = ..., convert_dates: Union[bool, None] = ..., convert_categoricals: Union[bool, None] = ..., index_col: Union[str, None] = ..., convert_missing: Union[bool, None] = ..., preserve_dtypes: Union[bool, None] = ..., columns: Union[Sequence[str], None] = ..., order_categoricals: Union[bool, None] = ...) -> DataFrame: ...
    @property
    def data_label(self) -> str: ...
    def variable_labels(self) -> dict[str, str]: ...
    def value_labels(self) -> dict[str, dict[Union[float, int], str]]: ...

def read_stata(filepath_or_buffer: Union[FilePath, ReadBuffer[bytes]], convert_dates: bool = ..., convert_categoricals: bool = ..., index_col: Union[str, None] = ..., convert_missing: bool = ..., preserve_dtypes: bool = ..., columns: Union[Sequence[str], None] = ..., order_categoricals: bool = ..., chunksize: Union[int, None] = ..., iterator: bool = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ...) -> Union[DataFrame, StataReader]: ...

class StataWriter(StataParser):
    data: Any
    storage_options: Any
    type_converters: Any
    def __init__(self, fname: Union[FilePath, WriteBuffer[bytes]], data: DataFrame, convert_dates: Union[dict[Hashable, str], None] = ..., write_index: bool = ..., byteorder: Union[str, None] = ..., time_stamp: Union[datetime.datetime, None] = ..., data_label: Union[str, None] = ..., variable_labels: Union[dict[Hashable, str], None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ..., *, value_labels: Union[dict[Hashable, dict[Union[float, int], str]], None] = ...) -> None: ...
    def write_file(self) -> None: ...

class StataStrLWriter:
    df: Any
    columns: Any
    def __init__(self, df: DataFrame, columns: Sequence[str], version: int = ..., byteorder: Union[str, None] = ...) -> None: ...
    def generate_table(self) -> tuple[dict[str, tuple[int, int]], DataFrame]: ...
    def generate_blob(self, gso_table: dict[str, tuple[int, int]]) -> bytes: ...

class StataWriter117(StataWriter):
    def __init__(self, fname: Union[FilePath, WriteBuffer[bytes]], data: DataFrame, convert_dates: Union[dict[Hashable, str], None] = ..., write_index: bool = ..., byteorder: Union[str, None] = ..., time_stamp: Union[datetime.datetime, None] = ..., data_label: Union[str, None] = ..., variable_labels: Union[dict[Hashable, str], None] = ..., convert_strl: Union[Sequence[Hashable], None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ..., *, value_labels: Union[dict[Hashable, dict[Union[float, int], str]], None] = ...) -> None: ...

class StataWriterUTF8(StataWriter117):
    def __init__(self, fname: Union[FilePath, WriteBuffer[bytes]], data: DataFrame, convert_dates: Union[dict[Hashable, str], None] = ..., write_index: bool = ..., byteorder: Union[str, None] = ..., time_stamp: Union[datetime.datetime, None] = ..., data_label: Union[str, None] = ..., variable_labels: Union[dict[Hashable, str], None] = ..., convert_strl: Union[Sequence[Hashable], None] = ..., version: Union[int, None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ..., *, value_labels: Union[dict[Hashable, dict[Union[float, int], str]], None] = ...) -> None: ...

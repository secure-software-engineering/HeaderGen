import numpy as np
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, FloatFormatType as FloatFormatType, IndexLabel as IndexLabel, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.generic import ABCDatetimeIndex as ABCDatetimeIndex, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCPeriodIndex as ABCPeriodIndex
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.api import Index as Index
from pandas.io.common import get_handle as get_handle
from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Union, Any, Hashable, Sequence

class CSVFormatter:
    cols: np.ndarray
    fmt: Any
    obj: Any
    filepath_or_buffer: Any
    encoding: Any
    compression: Any
    mode: Any
    storage_options: Any
    sep: Any
    index_label: Any
    errors: Any
    quoting: Any
    quotechar: Any
    doublequote: Any
    escapechar: Any
    line_terminator: Any
    date_format: Any
    chunksize: Any
    def __init__(self, formatter: DataFrameFormatter, path_or_buf: Union[FilePath, WriteBuffer[str], WriteBuffer[bytes]] = ..., sep: str = ..., cols: Union[Sequence[Hashable], None] = ..., index_label: Union[IndexLabel, None] = ..., mode: str = ..., encoding: Union[str, None] = ..., errors: str = ..., compression: CompressionOptions = ..., quoting: Union[int, None] = ..., line_terminator: Union[str, None] = ..., chunksize: Union[int, None] = ..., quotechar: Union[str, None] = ..., date_format: Union[str, None] = ..., doublequote: bool = ..., escapechar: Union[str, None] = ..., storage_options: StorageOptions = ...) -> None: ...
    @property
    def na_rep(self) -> str: ...
    @property
    def float_format(self) -> Union[FloatFormatType, None]: ...
    @property
    def decimal(self) -> str: ...
    @property
    def header(self) -> Union[bool, Sequence[str]]: ...
    @property
    def index(self) -> bool: ...
    @property
    def has_mi_columns(self) -> bool: ...
    def data_index(self) -> Index: ...
    @property
    def nlevels(self) -> int: ...
    @property
    def write_cols(self) -> Sequence[Hashable]: ...
    @property
    def encoded_labels(self) -> list[Hashable]: ...
    writer: Any
    def save(self) -> None: ...

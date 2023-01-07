import numpy as np
from datetime import tzinfo
from pandas import Interval as Interval
from pandas._libs import Period as Period, Timedelta as Timedelta, Timestamp as Timestamp
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy, GroupBy as GroupBy, SeriesGroupBy as SeriesGroupBy
from pandas.core.indexes.base import Index as Index
from pandas.core.internals import ArrayManager as ArrayManager, BlockManager as BlockManager, SingleArrayManager as SingleArrayManager, SingleBlockManager as SingleBlockManager
from pandas.core.resample import Resampler as Resampler
from pandas.core.series import Series as Series
from pandas.core.window.rolling import BaseWindow as BaseWindow
from pandas.io.formats.format import EngFormatter as EngFormatter
from pandas.tseries.offsets import DateOffset as DateOffset
from typing import Union, Any, Callable, Collection, Dict, Hashable, Iterator, List, Mapping, Optional, Sequence, Tuple, Type as type_t, TypeVar, Union

NumpyValueArrayLike: Any
NumpySorter: Any
ArrayLike: Any
AnyArrayLike: Any
PythonScalar = Union[str, int, float, bool]
DatetimeLikeScalar: Any
PandasScalar: Any
Scalar = Union[PythonScalar, PandasScalar]
IntStrT = TypeVar('IntStrT', int, str)
TimestampConvertibleTypes: Any
TimedeltaConvertibleTypes: Any
Timezone = Union[str, tzinfo]
NDFrameT = TypeVar('NDFrameT', bound='DataFrame')
Axis = Union[str, int]
IndexLabel = Union[Hashable, Sequence[Hashable]]
Level = Union[Hashable, int]
Shape = Tuple[int, ...]
Suffixes = Tuple[Optional[str], Optional[str]]
Ordered = Optional[bool]
JSONSerializable = Optional[Union[PythonScalar, List, Dict]]
Frequency: Any
Axes = Collection[Any]
RandomState: Any
NpDtype = Union[str, np.dtype, type_t[Union[str, float, int, complex, bool, object]]]
Dtype: Any
AstypeArg: Any
DtypeArg = Union[Dtype, Dict[Hashable, Dtype]]
DtypeObj: Any
Renamer = Union[Mapping[Hashable, Any], Callable[[Hashable], Hashable]]
T = TypeVar('T')
FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)
ValueKeyFunc: Any
IndexKeyFunc: Any
AggFuncTypeBase = Union[Callable, str]
AggFuncTypeDict = Dict[Hashable, Union[AggFuncTypeBase, List[AggFuncTypeBase]]]
AggFuncType = Union[AggFuncTypeBase, List[AggFuncTypeBase], AggFuncTypeDict]
AggObjType: Any
PythonFuncType = Callable[[Any], Any]
AnyStr_cov = TypeVar('AnyStr_cov', str, bytes, covariant=True)
AnyStr_con = TypeVar('AnyStr_con', str, bytes, contravariant=True)

class BaseBuffer:
    @property
    def mode(self) -> str: ...
    def fileno(self) -> int: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...

class ReadBuffer(BaseBuffer):
    def read(self, __n: Union[int, None] = ...) -> AnyStr_cov: ...

class WriteBuffer(BaseBuffer):
    def write(self, __b: AnyStr_con) -> Any: ...
    def flush(self) -> Any: ...

class ReadPickleBuffer(ReadBuffer[bytes]):
    def readline(self) -> AnyStr_cov: ...

class WriteExcelBuffer(WriteBuffer[bytes]):
    def truncate(self, size: Union[int, None] = ...) -> int: ...

class ReadCsvBuffer(ReadBuffer[AnyStr_cov]):
    def __iter__(self) -> Iterator[AnyStr_cov]: ...
    def readline(self) -> AnyStr_cov: ...
    @property
    def closed(self) -> bool: ...

FilePath: Any
StorageOptions = Optional[Dict[str, Any]]
CompressionDict = Dict[str, Any]
CompressionOptions: Any
XMLParsers: Any
FormattersType = Union[List[Callable], Tuple[Callable, ...], Mapping[Union[str, int], Callable]]
ColspaceType = Mapping[Hashable, Union[str, int]]
FloatFormatType: Any
ColspaceArgType = Union[str, int, Sequence[Union[str, int]], Mapping[Hashable, Union[str, int]]]
FillnaOptions: Any
Manager: Any
SingleManager: Any
Manager2D: Any
ScalarIndexer = Union[int, np.integer]
SequenceIndexer = Union[slice, List[int], np.ndarray]
PositionalIndexer = Union[ScalarIndexer, SequenceIndexer]
PositionalIndexerTuple = Tuple[PositionalIndexer, PositionalIndexer]
PositionalIndexer2D = Union[PositionalIndexer, PositionalIndexerTuple]
TakeIndexer: Any
WindowingRankType: Any
CSVEngine: Any

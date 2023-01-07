from numpy import bool_ as bool_, byte as byte, bytes_ as bytes_, cdouble as cdouble, clongdouble as clongdouble, csingle as csingle, datetime64 as datetime64, double as double, dtype as dtype, generic as generic, half as half, int_ as int_, intc as intc, longdouble as longdouble, longlong as longlong, ndarray as ndarray, object_ as object_, short as short, single as single, str_ as str_, timedelta64 as timedelta64, ubyte as ubyte, uint as uint, uintc as uintc, ulonglong as ulonglong, ushort as ushort, void as void
from numpy.typing import ArrayLike as ArrayLike, DTypeLike as DTypeLike
from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union, overload
from typing_extensions import Literal, Protocol as Protocol, TypedDict

class _CastFunc:
    def __call__(self, x: ArrayLike, k: DTypeLike = ...) -> ndarray[Any, dtype[Any]]: ...

class _TypeCodes(TypedDict):
    Character: Literal[c]
    Integer: Literal[bhilqp]
    UnsignedInteger: Literal[BHILQP]
    Float: Literal[efdg]
    Complex: Literal[FDG]
    AllInteger: Literal[bBhHiIlLqQpP]
    AllFloat: Literal[efdgFDG]
    Datetime: Literal[Mm]
    All: Literal['?bhilqpBHILQPefdgFDGSUVOMm']

class _typedict(Dict[Type[generic], _T]):
    def __getitem__(self, key: DTypeLike) -> _T: ...

def maximum_sctype(t: DTypeLike) -> dtype: ...
def issctype(rep: object) -> bool: ...
@overload
def obj2sctype(rep: object) -> Optional[generic]: ...
@overload
def obj2sctype(rep: object, default: None) -> Optional[generic]: ...
@overload
def obj2sctype(rep: object, default: Type[_T]) -> Union[generic, Type[_T]]: ...
def issubclass_(arg1: object, arg2: Union[object, Tuple[object, ...]]) -> bool: ...
def issubsctype(arg1: Union[ndarray, DTypeLike], arg2: Union[ndarray, DTypeLike]) -> bool: ...
def issubdtype(arg1: DTypeLike, arg2: DTypeLike) -> bool: ...
def sctype2char(sctype: object) -> str: ...
def find_common_type(array_types: Sequence[DTypeLike], scalar_types: Sequence[DTypeLike]) -> dtype: ...

cast: _typedict[_CastFunc]
nbytes: _typedict[int]
typecodes: _TypeCodes
ScalarType: Tuple[Type[int], Type[float], Type[complex], Type[int], Type[bool], Type[bytes], Type[str], Type[memoryview], Type[bool_], Type[csingle], Type[cdouble], Type[clongdouble], Type[half], Type[single], Type[double], Type[longdouble], Type[byte], Type[short], Type[intc], Type[int_], Type[longlong], Type[timedelta64], Type[datetime64], Type[object_], Type[bytes_], Type[str_], Type[ubyte], Type[ushort], Type[uintc], Type[uint], Type[ulonglong], Type[void]]

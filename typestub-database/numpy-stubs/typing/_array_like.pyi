from ._dtype_like import DTypeLike as DTypeLike
from numpy import bool_ as bool_, bytes_ as bytes_, complexfloating as complexfloating, datetime64 as datetime64, dtype as dtype, floating as floating, generic as generic, integer as integer, ndarray as ndarray, number as number, object_ as object_, str_ as str_, timedelta64 as timedelta64, unsignedinteger as unsignedinteger, void as void
from typing import Any
from typing_extensions import Protocol as Protocol

HAVE_PROTOCOL: bool

class _SupportsArray:
    def __array__(self) -> ndarray[Any, _DType_co]: ...

ArrayLike: Any

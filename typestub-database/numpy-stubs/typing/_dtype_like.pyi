from typing import Any, Sequence
from typing_extensions import Protocol as Protocol, TypedDict

HAVE_PROTOCOL: bool

class _DTypeDictBase(TypedDict):
    names: Sequence[str]
    formats: Sequence[_DTypeLikeNested]

class _DTypeDict(_DTypeDictBase):
    offsets: Sequence[int]
    titles: Sequence[Any]
    itemsize: int
    aligned: bool

class _SupportsDType:
    @property
    def dtype(self) -> _DType_co: ...

DTypeLike: Any

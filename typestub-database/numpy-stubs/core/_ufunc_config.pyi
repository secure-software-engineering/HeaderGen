from typing import Any, Optional, Union
from typing_extensions import Protocol as Protocol, TypedDict

class _SupportsWrite:
    def write(self, __msg: str) -> Any: ...

class _ErrDict(TypedDict):
    divide: _ErrKind
    over: _ErrKind
    under: _ErrKind
    invalid: _ErrKind

class _ErrDictOptional(TypedDict):
    all: Optional[_ErrKind]
    divide: Optional[_ErrKind]
    over: Optional[_ErrKind]
    under: Optional[_ErrKind]
    invalid: Optional[_ErrKind]

def seterr(all: Optional[_ErrKind] = ..., divide: Optional[_ErrKind] = ..., over: Optional[_ErrKind] = ..., under: Optional[_ErrKind] = ..., invalid: Optional[_ErrKind] = ...) -> _ErrDict: ...
def geterr() -> _ErrDict: ...
def setbufsize(size: int) -> int: ...
def getbufsize() -> int: ...
def seterrcall(func: Union[None, _ErrFunc, _SupportsWrite]) -> Union[None, _ErrFunc, _SupportsWrite]: ...
def geterrcall() -> Union[None, _ErrFunc, _SupportsWrite]: ...

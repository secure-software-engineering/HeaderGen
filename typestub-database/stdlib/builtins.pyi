# builtins.pyi

from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

T = TypeVar("T")
S = TypeVar("S", bound=Sequence[T])
U = TypeVar("U", bound=Iterable[T])

def len(s: Union[S, Iterable]) -> int: ...
def sum(
    iterable: Iterable[Union[int, float, T]], start: Optional[Union[int, float]] = None
) -> Union[int, float, T]: ...
def max(
    arg1: U,
    arg2: Optional[Iterable[T]] = None,
    *args: Any,
    key: Optional[Callable[[T], Any]] = None,
    default: Optional[Any] = None
) -> T: ...
def min(
    arg1: U,
    arg2: Optional[Iterable[T]] = None,
    *args: Any,
    key: Optional[Callable[[T], Any]] = None,
    default: Optional[Any] = None
) -> T: ...
def sorted(
    iterable: Iterable[T],
    *,
    key: Optional[Callable[[T], Any]] = None,
    reverse: bool = False
) -> List[T]: ...
def any(iterable: Iterable[Any]) -> bool: ...
def all(iterable: Iterable[Any]) -> bool: ...

# ... other classes and functions ...

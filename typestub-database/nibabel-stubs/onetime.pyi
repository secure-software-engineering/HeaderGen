import typing as ty

from _typeshed import Incomplete
from nibabel.deprecated import deprecate_with_version as deprecate_with_version

InstanceT = ty.TypeVar("InstanceT")
T = ty.TypeVar("T")

class ResetMixin:
    def reset(self) -> None: ...

class OneTimeProperty(ty.Generic[T]):
    getter: Incomplete
    name: Incomplete
    __doc__: Incomplete
    def __init__(self, func: ty.Callable[[InstanceT], T]) -> None: ...
    @ty.overload
    def __get__(
        self, obj: None, objtype: type[InstanceT] | None = None
    ) -> ty.Callable[[InstanceT], T]: ...
    @ty.overload
    def __get__(self, obj: InstanceT, objtype: type[InstanceT] | None = None) -> T: ...

def auto_attr(func: ty.Callable[[InstanceT], T]) -> OneTimeProperty[T]: ...

setattr_on_read: Incomplete

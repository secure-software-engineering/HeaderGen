import typing as ty

from _typeshed import Incomplete

T = ty.TypeVar("T")
P = ty.ParamSpec("P")
TESTSETUP: str
TESTCLEANUP: str

class ExpiredDeprecationError(RuntimeError): ...

class Deprecator:
    version_comparator: Incomplete
    warn_class: Incomplete
    error_class: Incomplete
    def __init__(
        self,
        version_comparator: ty.Callable[[str], int],
        warn_class: type[Warning] = ...,
        error_class: type[Exception] = ...,
    ) -> None: ...
    def is_bad_version(self, version_str: str) -> bool: ...
    def __call__(
        self,
        message: str,
        since: str = "",
        until: str = "",
        warn_class: type[Warning] | None = None,
        error_class: type[Exception] | None = None,
    ) -> ty.Callable[[ty.Callable[P, T]], ty.Callable[P, T]]: ...

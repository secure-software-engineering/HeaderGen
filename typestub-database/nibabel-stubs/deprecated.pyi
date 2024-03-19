import typing as ty

from _typeshed import Incomplete

from .deprecator import Deprecator as Deprecator
from .pkg_info import cmp_pkg_version as cmp_pkg_version

P = ty.ParamSpec("P")

class ModuleProxy:
    def __init__(self, module_name: str) -> None: ...
    def __getattr__(self, key: str) -> ty.Any: ...

class FutureWarningMixin:
    warn_message: str
    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None: ...

class VisibleDeprecationWarning(UserWarning): ...

deprecate_with_version: Incomplete

def alert_future_error(
    msg: str,
    version: str,
    *,
    warning_class: type[Warning] = ...,
    error_class: type[Exception] = ...,
    warning_rec: str = "",
    error_rec: str = "",
    stacklevel: int = 2
) -> None: ...

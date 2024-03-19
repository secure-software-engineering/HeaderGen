import typing as ty
from types import ModuleType

from packaging.version import Version

from .tripwire import TripWire as TripWire

def optional_package(
    name: str,
    trip_msg: str | None = None,
    min_version: str | Version | ty.Callable[[ModuleType], bool] | None = None,
) -> tuple[ModuleType | TripWire, bool, ty.Callable[[], None]]: ...

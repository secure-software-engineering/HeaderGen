from matplotlib import cbook as cbook
from typing import Any

class ConversionError(TypeError): ...

class AxisInfo:
    majloc: Any
    minloc: Any
    majfmt: Any
    minfmt: Any
    label: Any
    default_limits: Any
    def __init__(self, majloc: Any | None = ..., minloc: Any | None = ..., majfmt: Any | None = ..., minfmt: Any | None = ..., label: Any | None = ..., default_limits: Any | None = ...) -> None: ...

class ConversionInterface:
    @staticmethod
    def axisinfo(unit, axis) -> None: ...
    @staticmethod
    def default_units(x, axis) -> None: ...
    @staticmethod
    def convert(obj, unit, axis): ...
    @staticmethod
    def is_numlike(x): ...

class DecimalConverter(ConversionInterface):
    @staticmethod
    def convert(value, unit, axis): ...

class Registry(dict):
    def get_converter(self, x): ...

registry: Any

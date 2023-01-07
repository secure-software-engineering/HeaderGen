import matplotlib.units as units
from typing import Any

class UnitDblConverter(units.ConversionInterface):
    defaults: Any
    @staticmethod
    def axisinfo(unit, axis): ...
    @staticmethod
    def convert(value, unit, axis): ...
    @staticmethod
    def default_units(value, axis): ...

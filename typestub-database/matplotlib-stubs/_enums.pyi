from enum import Enum
from matplotlib import docstring as docstring
from typing import Any

class _AutoStringNameEnum(Enum):
    def __hash__(self): ...

class JoinStyle(str, _AutoStringNameEnum):
    miter: Any
    round: Any
    bevel: Any
    @staticmethod
    def demo() -> None: ...

class CapStyle(str, _AutoStringNameEnum):
    butt: str
    projecting: str
    round: str
    @staticmethod
    def demo() -> None: ...

from matplotlib import docstring as docstring
from matplotlib.patches import PathPatch as PathPatch
from matplotlib.path import Path as Path
from matplotlib.transforms import Affine2D as Affine2D
from typing import Any

__credits__: Any
RIGHT: int
UP: int
DOWN: int

class Sankey:
    diagrams: Any
    ax: Any
    unit: Any
    format: Any
    scale: Any
    gap: Any
    radius: Any
    shoulder: Any
    offset: Any
    margin: Any
    pitch: Any
    tolerance: Any
    extent: Any
    def __init__(self, ax: Any | None = ..., scale: float = ..., unit: str = ..., format: str = ..., gap: float = ..., radius: float = ..., shoulder: float = ..., offset: float = ..., head_angle: int = ..., margin: float = ..., tolerance: float = ..., **kwargs) -> None: ...
    def add(self, patchlabel: str = ..., flows: Any | None = ..., orientations: Any | None = ..., labels: str = ..., trunklength: float = ..., pathlengths: float = ..., prior: Any | None = ..., connect=..., rotation: int = ..., **kwargs): ...
    def finish(self): ...

from matplotlib.path import Path as Path
from typing import Any

class HatchPatternBase: ...

class HorizontalHatch(HatchPatternBase):
    num_lines: Any
    num_vertices: Any
    def __init__(self, hatch, density) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class VerticalHatch(HatchPatternBase):
    num_lines: Any
    num_vertices: Any
    def __init__(self, hatch, density) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class NorthEastHatch(HatchPatternBase):
    num_lines: Any
    num_vertices: Any
    def __init__(self, hatch, density) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class SouthEastHatch(HatchPatternBase):
    num_lines: Any
    num_vertices: Any
    def __init__(self, hatch, density) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class Shapes(HatchPatternBase):
    filled: bool
    num_shapes: int
    num_vertices: int
    def __init__(self, hatch, density) -> None: ...
    def set_vertices_and_codes(self, vertices, codes) -> None: ...

class Circles(Shapes):
    shape_vertices: Any
    shape_codes: Any
    def __init__(self, hatch, density) -> None: ...

class SmallCircles(Circles):
    size: float
    num_rows: Any
    def __init__(self, hatch, density) -> None: ...

class LargeCircles(Circles):
    size: float
    num_rows: Any
    def __init__(self, hatch, density) -> None: ...

class SmallFilledCircles(Circles):
    size: float
    filled: bool
    num_rows: Any
    def __init__(self, hatch, density) -> None: ...

class Stars(Shapes):
    size: Any
    filled: bool
    num_rows: Any
    shape_vertices: Any
    shape_codes: Any
    def __init__(self, hatch, density) -> None: ...

def get_path(hatchpattern, density: int = ...): ...

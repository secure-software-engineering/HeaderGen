from matplotlib.artist import Artist as Artist
from typing import Any

class Container(tuple):
    def __new__(cls, *args, **kwargs): ...
    def __init__(self, kl, label: Any | None = ...) -> None: ...
    def remove(self): ...
    def get_children(self): ...
    get_label: Any
    set_label: Any
    add_callback: Any
    remove_callback: Any
    pchanged: Any

class BarContainer(Container):
    patches: Any
    errorbar: Any
    datavalues: Any
    orientation: Any
    def __init__(self, patches, errorbar: Any | None = ..., *, datavalues: Any | None = ..., orientation: Any | None = ..., **kwargs) -> None: ...

class ErrorbarContainer(Container):
    lines: Any
    has_xerr: Any
    has_yerr: Any
    def __init__(self, lines, has_xerr: bool = ..., has_yerr: bool = ..., **kwargs) -> None: ...

class StemContainer(Container):
    markerline: Any
    stemlines: Any
    baseline: Any
    def __init__(self, markerline_stemlines_baseline, **kwargs) -> None: ...

from matplotlib import cbook as cbook
from typing import Any, NamedTuple

class Page(NamedTuple):
    text: Any
    boxes: Any
    height: Any
    width: Any
    descent: Any

class Text(NamedTuple):
    x: Any
    y: Any
    font: Any
    glyph: Any
    width: Any

class Box(NamedTuple):
    x: Any
    y: Any
    height: Any
    width: Any

class Dvi:
    file: Any
    dpi: Any
    fonts: Any
    state: Any
    def __init__(self, filename, dpi) -> None: ...
    baseline: Any
    def __enter__(self): ...
    def __exit__(self, etype, evalue, etrace) -> None: ...
    def __iter__(self): ...
    def close(self) -> None: ...

class DviFont:
    texname: Any
    size: Any
    widths: Any
    def __init__(self, scale, tfm, texname, vf) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Vf(Dvi):
    def __init__(self, filename) -> None: ...
    def __getitem__(self, code): ...

class Tfm:
    def __init__(self, filename) -> None: ...

class PsFont(NamedTuple):
    texname: Any
    psname: Any
    effects: Any
    encoding: Any
    filename: Any

class PsfontsMap:
    def __new__(cls, filename): ...
    def __getitem__(self, texname): ...

class _LuatexKpsewhich:
    def __new__(cls): ...
    def search(self, filename): ...

def find_tex_file(filename, format: Any | None = ...): ...

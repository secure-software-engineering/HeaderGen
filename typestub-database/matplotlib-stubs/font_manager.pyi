import json
from matplotlib import afm as afm, cbook as cbook, ft2font as ft2font, rcParams as rcParams
from matplotlib.fontconfig_pattern import generate_fontconfig_pattern as generate_fontconfig_pattern, parse_fontconfig_pattern as parse_fontconfig_pattern
from typing import Any

font_scalings: Any
stretch_dict: Any
weight_dict: Any
font_family_aliases: Any
MSFolders: str
MSFontDirectories: Any
MSUserFontDirectories: Any
X11FontDirectories: Any
OSXFontDirectories: Any

def get_fontext_synonyms(fontext): ...
def list_fonts(directory, extensions): ...
def win32FontDirectory(): ...
def win32InstalledFonts(directory: Any | None = ..., fontext: str = ...): ...
def get_fontconfig_fonts(fontext: str = ...): ...
def findSystemFonts(fontpaths: Any | None = ..., fontext: str = ...): ...

FontEntry: Any

def ttfFontProperty(font): ...
def afmFontProperty(fontpath, font): ...

class FontProperties:
    def __init__(self, family: Any | None = ..., style: Any | None = ..., variant: Any | None = ..., weight: Any | None = ..., stretch: Any | None = ..., size: Any | None = ..., fname: Any | None = ..., math_fontfamily: Any | None = ...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def get_family(self): ...
    def get_name(self): ...
    def get_style(self): ...
    get_slant: Any
    def get_variant(self): ...
    def get_weight(self): ...
    def get_stretch(self): ...
    def get_size(self): ...
    def get_size_in_points(self): ...
    def get_file(self): ...
    def get_fontconfig_pattern(self): ...
    def set_family(self, family) -> None: ...
    set_name: Any
    def set_style(self, style) -> None: ...
    set_slant: Any
    def set_variant(self, variant) -> None: ...
    def set_weight(self, weight) -> None: ...
    def set_stretch(self, stretch) -> None: ...
    def set_size(self, size) -> None: ...
    def set_file(self, file) -> None: ...
    def set_fontconfig_pattern(self, pattern) -> None: ...
    def get_math_fontfamily(self): ...
    def set_math_fontfamily(self, fontfamily) -> None: ...
    def copy(self): ...

class _JSONEncoder(json.JSONEncoder):
    def default(self, o): ...

def json_dump(data, filename) -> None: ...
def json_load(filename): ...

class FontManager:
    default_size: Any
    defaultFamily: Any
    afmlist: Any
    ttflist: Any
    def __init__(self, size: Any | None = ..., weight: str = ...): ...
    def addfont(self, path) -> None: ...
    @property
    def defaultFont(self): ...
    def get_default_weight(self): ...
    @staticmethod
    def get_default_size(): ...
    def set_default_weight(self, weight) -> None: ...
    def score_family(self, families, family2): ...
    def score_style(self, style1, style2): ...
    def score_variant(self, variant1, variant2): ...
    def score_stretch(self, stretch1, stretch2): ...
    def score_weight(self, weight1, weight2): ...
    def score_size(self, size1, size2): ...
    def findfont(self, prop, fontext: str = ..., directory: Any | None = ..., fallback_to_default: bool = ..., rebuild_if_missing: bool = ...): ...

def is_opentype_cff_font(filename): ...
def get_font(filename, hinting_factor: Any | None = ...): ...

fontManager: Any
findfont: Any

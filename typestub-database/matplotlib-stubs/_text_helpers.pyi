from .ft2font import KERNING_DEFAULT as KERNING_DEFAULT, LOAD_NO_HINTING as LOAD_NO_HINTING
from typing import Any

LayoutItem: Any

def warn_on_missing_glyph(codepoint) -> None: ...
def layout(string, font, *, kern_mode=...) -> None: ...

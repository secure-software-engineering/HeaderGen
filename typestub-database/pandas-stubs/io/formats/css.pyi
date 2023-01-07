from typing import Union, Any

class CSSWarning(UserWarning): ...

class CSSResolver:
    UNIT_RATIOS: Any
    FONT_SIZE_RATIOS: Any
    MARGIN_RATIOS: Any
    BORDER_WIDTH_RATIOS: Any
    SIDE_SHORTHANDS: Any
    SIDES: Any
    def __call__(self, declarations_str: str, inherited: Union[dict[str, str], None] = ...) -> dict[str, str]: ...
    def size_to_pt(self, in_val, em_pt: Any | None = ..., conversions=...): ...
    def atomize(self, declarations) -> None: ...
    expand_border_color: Any
    expand_border_style: Any
    expand_border_width: Any
    expand_margin: Any
    expand_padding: Any
    def parse(self, declarations_str: str): ...

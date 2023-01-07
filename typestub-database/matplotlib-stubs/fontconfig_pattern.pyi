from typing import Any

family_punc: str
family_unescape: Any
family_escape: Any
value_punc: str
value_unescape: Any
value_escape: Any

class FontconfigPatternParser:
    ParseException: Any
    def __init__(self) -> None: ...
    def parse(self, pattern): ...

parse_fontconfig_pattern: Any

def generate_fontconfig_pattern(d): ...

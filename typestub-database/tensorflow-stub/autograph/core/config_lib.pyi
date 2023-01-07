import enum

class Rule:
    def __init__(self, module_prefix) -> None: ...
    def matches(self, module_name): ...

class Action(enum.Enum):
    NONE: int
    CONVERT: int
    DO_NOT_CONVERT: int

class DoNotConvert(Rule):
    def get_action(self, module): ...

class Convert(Rule):
    def get_action(self, module): ...

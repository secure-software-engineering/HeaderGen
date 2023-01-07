import enum
from typing import Any

class NoValue(enum.Enum):
    def of(self, node, default: Any | None = ...): ...
    def add_to(self, node, value) -> None: ...
    def exists(self, node): ...

class Basic(NoValue):
    QN: str
    SKIP_PROCESSING: str
    INDENT_BLOCK_REMAINDER: str
    ORIGIN: str
    DIRECTIVES: str
    EXTRA_LOOP_TEST: str

class Static(NoValue):
    IS_PARAM: str
    SCOPE: str
    ARGS_SCOPE: str
    COND_SCOPE: str
    BODY_SCOPE: str
    ORELSE_SCOPE: str
    DEFINITIONS: str
    ORIG_DEFINITIONS: str
    DEFINED_FNS_IN: str
    DEFINED_VARS_IN: str
    LIVE_VARS_OUT: str
    LIVE_VARS_IN: str
    TYPES: str
    CLOSURE_TYPES: str
    VALUE: str

FAIL: Any

def keys(node, field_name: str = ...): ...
def getanno(node, key, default=..., field_name: str = ...): ...
def hasanno(node, key, field_name: str = ...): ...
def setanno(node, key, value, field_name: str = ...) -> None: ...
def delanno(node, key, field_name: str = ...) -> None: ...
def copyanno(from_node, to_node, key, field_name: str = ...) -> None: ...
def dup(node, copy_map, field_name: str = ...) -> None: ...

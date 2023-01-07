from enum import Enum

class NoValue(Enum): ...

class NodeAnno(NoValue):
    IS_LOCAL: str
    IS_PARAM: str
    IS_MODIFIED_SINCE_ENTRY: str
    ARGS_SCOPE: str
    COND_SCOPE: str
    ITERATE_SCOPE: str
    ARGS_AND_BODY_SCOPE: str
    BODY_SCOPE: str
    ORELSE_SCOPE: str

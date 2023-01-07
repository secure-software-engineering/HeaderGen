from statsmodels.tools.tools import Bunch as Bunch
from typing import Any

PARAM_LIST: Any

def bunch_factory(attribute, columns): ...

ParamsTableTestBunch: Any
MarginTableTestBunch: Any

class Holder:
    def __init__(self, **kwds) -> None: ...

def assert_equal(actual, desired, err_msg: str = ..., verbose: bool = ..., **kwds) -> None: ...

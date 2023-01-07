from .auxfuncs import applyrules as applyrules, dictappend as dictappend, gentitle as gentitle, hasnote as hasnote, outmess as outmess
from typing import Any

f2py_version: str
usemodule_rules: Any

def buildusevars(m, r): ...
def buildusevar(name, realname, vars, usemodulename): ...

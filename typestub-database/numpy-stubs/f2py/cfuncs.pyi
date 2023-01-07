from typing import Any

f2py_version: Any
errmess: Any
outneeds: Any
needs: Any
includes0: Any
includes: Any
userincludes: Any
typedefs: Any
typedefs_generated: Any
cppmacros: Any
cfuncs: Any
callbacks: Any
f90modhooks: Any
commonhooks: Any

def buildcfuncs() -> None: ...
def append_needs(need, flag: int = ...): ...
def get_needs(): ...

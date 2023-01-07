from .auxfuncs import *
from . import capi_maps as capi_maps, func2subr as func2subr
from .crackfortran import undo_rmbadname as undo_rmbadname, undo_rmbadname1 as undo_rmbadname1
from typing import Any

f2py_version: str
options: Any

def findf90modules(m): ...

fgetdims1: Any
fgetdims2: str
fgetdims2_sa: str

def buildhooks(pymod): ...

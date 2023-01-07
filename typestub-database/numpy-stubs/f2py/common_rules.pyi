from . import capi_maps as capi_maps, func2subr as func2subr
from .auxfuncs import hasbody as hasbody, hascommon as hascommon, hasnote as hasnote, isintent_hide as isintent_hide, outmess as outmess
from .crackfortran import rmbadname as rmbadname
from typing import Any

f2py_version: Any

def findcommonblocks(block, top: int = ...): ...
def buildhooks(m): ...

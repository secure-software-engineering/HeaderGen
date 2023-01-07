from . import cfuncs as cfuncs
from .auxfuncs import applyrules as applyrules, debugcapi as debugcapi, dictappend as dictappend, errmess as errmess, getargs as getargs, hasnote as hasnote, isarray as isarray, iscomplex as iscomplex, iscomplexarray as iscomplexarray, iscomplexfunction as iscomplexfunction, isfunction as isfunction, isintent_c as isintent_c, isintent_hide as isintent_hide, isintent_in as isintent_in, isintent_inout as isintent_inout, isintent_nothide as isintent_nothide, isintent_out as isintent_out, isoptional as isoptional, isrequired as isrequired, isscalar as isscalar, isstring as isstring, isstringfunction as isstringfunction, issubroutine as issubroutine, l_and as l_and, l_not as l_not, l_or as l_or, outmess as outmess, replace as replace, stripcomma as stripcomma, throw_error as throw_error
from typing import Any

f2py_version: Any
cb_routine_rules: Any
cb_rout_rules: Any
cb_arg_rules: Any
cb_map: Any

def buildcallbacks(m) -> None: ...
def buildcallback(rout, um) -> None: ...

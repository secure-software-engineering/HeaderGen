from . import capi_maps as capi_maps, cfuncs as cfuncs, common_rules as common_rules, f90mod_rules as f90mod_rules, func2subr as func2subr, use_rules as use_rules
from .auxfuncs import applyrules as applyrules, debugcapi as debugcapi, dictappend as dictappend, errmess as errmess, gentitle as gentitle, getargs2 as getargs2, hascallstatement as hascallstatement, hasexternals as hasexternals, hasinitvalue as hasinitvalue, hasnote as hasnote, hasresultnote as hasresultnote, isarray as isarray, isarrayofstrings as isarrayofstrings, iscomplex as iscomplex, iscomplexarray as iscomplexarray, iscomplexfunction as iscomplexfunction, iscomplexfunction_warn as iscomplexfunction_warn, isdummyroutine as isdummyroutine, isexternal as isexternal, isfunction as isfunction, isfunction_wrap as isfunction_wrap, isint1array as isint1array, isintent_aux as isintent_aux, isintent_c as isintent_c, isintent_callback as isintent_callback, isintent_copy as isintent_copy, isintent_hide as isintent_hide, isintent_inout as isintent_inout, isintent_nothide as isintent_nothide, isintent_out as isintent_out, isintent_overwrite as isintent_overwrite, islogical as islogical, islong_complex as islong_complex, islong_double as islong_double, islong_doublefunction as islong_doublefunction, islong_long as islong_long, islong_longfunction as islong_longfunction, ismoduleroutine as ismoduleroutine, isoptional as isoptional, isrequired as isrequired, isscalar as isscalar, issigned_long_longarray as issigned_long_longarray, isstring as isstring, isstringarray as isstringarray, isstringfunction as isstringfunction, issubroutine as issubroutine, issubroutine_wrap as issubroutine_wrap, isthreadsafe as isthreadsafe, isunsigned as isunsigned, isunsigned_char as isunsigned_char, isunsigned_chararray as isunsigned_chararray, isunsigned_long_long as isunsigned_long_long, isunsigned_long_longarray as isunsigned_long_longarray, isunsigned_short as isunsigned_short, isunsigned_shortarray as isunsigned_shortarray, l_and as l_and, l_not as l_not, l_or as l_or, outmess as outmess, replace as replace, requiresf90wrapper as requiresf90wrapper, stripcomma as stripcomma
from typing import Any

f2py_version: Any
numpy_version: Any
options: Any
sepdict: Any
generationtime: Any
module_rules: Any
defmod_rules: Any
routine_rules: Any
rout_rules: Any
typedef_need_dict: Any
aux_rules: Any
arg_rules: Any
check_rules: Any

def buildmodule(m, um): ...

stnd: Any

def buildapi(rout): ...

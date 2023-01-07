from distutils.extension import Extension as old_Extension
from typing import Any

cxx_ext_re: Any
fortran_pyf_ext_re: Any

class Extension(old_Extension):
    sources: Any
    swig_opts: Any
    depends: Any
    language: Any
    f2py_options: Any
    module_dirs: Any
    extra_f77_compile_args: Any
    extra_f90_compile_args: Any
    def __init__(self, name, sources, include_dirs: Any | None = ..., define_macros: Any | None = ..., undef_macros: Any | None = ..., library_dirs: Any | None = ..., libraries: Any | None = ..., runtime_library_dirs: Any | None = ..., extra_objects: Any | None = ..., extra_compile_args: Any | None = ..., extra_link_args: Any | None = ..., export_symbols: Any | None = ..., swig_opts: Any | None = ..., depends: Any | None = ..., language: Any | None = ..., f2py_options: Any | None = ..., module_dirs: Any | None = ..., extra_f77_compile_args: Any | None = ..., extra_f90_compile_args: Any | None = ...) -> None: ...
    def has_cxx_sources(self): ...
    def has_f2py_sources(self): ...

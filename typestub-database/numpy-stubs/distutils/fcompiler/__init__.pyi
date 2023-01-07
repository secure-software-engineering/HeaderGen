from numpy.distutils.ccompiler import CCompiler
from typing import Any

__metaclass__ = type

class CompilerNotFound(Exception): ...

class FCompiler(CCompiler):
    distutils_vars: Any
    command_vars: Any
    flag_vars: Any
    language_map: Any
    language_order: Any
    compiler_type: Any
    compiler_aliases: Any
    version_pattern: Any
    possible_executables: Any
    executables: Any
    suggested_f90_compiler: Any
    compile_switch: str
    object_switch: str
    library_switch: str
    module_dir_switch: Any
    module_include_switch: str
    pic_flags: Any
    src_extensions: Any
    obj_extension: str
    shared_lib_extension: Any
    static_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    c_compiler: Any
    extra_f77_compile_args: Any
    extra_f90_compile_args: Any
    def __init__(self, *args, **kw) -> None: ...
    def __copy__(self): ...
    def copy(self): ...
    version_cmd: Any
    compiler_f77: Any
    compiler_f90: Any
    compiler_fix: Any
    linker_so: Any
    linker_exe: Any
    archiver: Any
    ranlib: Any
    def set_executable(self, key, value) -> None: ...
    def set_commands(self, **kw) -> None: ...
    def set_command(self, key, value) -> None: ...
    def find_executables(self): ...
    def update_executables(self) -> None: ...
    def get_flags(self): ...
    def get_flags_f77(self): ...
    def get_flags_f90(self): ...
    def get_flags_free(self): ...
    def get_flags_fix(self): ...
    def get_flags_linker_so(self): ...
    def get_flags_linker_exe(self): ...
    def get_flags_ar(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_debug(self): ...
    get_flags_opt_f77: Any
    get_flags_opt_f90: Any
    get_flags_arch_f77: Any
    get_flags_arch_f90: Any
    get_flags_debug_f77: Any
    get_flags_debug_f90: Any
    def get_libraries(self): ...
    def get_library_dirs(self): ...
    def get_version(self, force: bool = ..., ok_status=...): ...
    def customize(self, dist: Any | None = ...) -> None: ...
    def dump_properties(self) -> None: ...
    def module_options(self, module_dirs, module_build_dir): ...
    def library_option(self, lib): ...
    def library_dir_option(self, dir): ...
    def link(self, target_desc, objects, output_filename, output_dir: Any | None = ..., libraries: Any | None = ..., library_dirs: Any | None = ..., runtime_library_dirs: Any | None = ..., export_symbols: Any | None = ..., debug: int = ..., extra_preargs: Any | None = ..., extra_postargs: Any | None = ..., build_temp: Any | None = ..., target_lang: Any | None = ...) -> None: ...
    def can_ccompiler_link(self, ccompiler): ...
    def wrap_unlinkable_objects(self, objects, output_dir, extra_dll_dir) -> None: ...

def new_fcompiler(plat: Any | None = ..., compiler: Any | None = ..., verbose: int = ..., dry_run: int = ..., force: int = ..., requiref90: bool = ..., c_compiler: Any | None = ...): ...
def show_fcompilers(dist: Any | None = ...) -> None: ...
def dummy_fortran_file(): ...

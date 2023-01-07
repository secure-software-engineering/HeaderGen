from distutils.errors import DistutilsPlatformError as DistutilsPlatformError
from numpy.distutils.fcompiler import FCompiler as FCompiler
from typing import Any

compilers: Any

class CompaqFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    fc_exe: str
    executables: Any
    module_dir_switch: str
    module_include_switch: str
    def get_flags(self): ...
    def get_flags_debug(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_linker_so(self): ...

class CompaqVisualFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    compile_switch: str
    object_switch: str
    library_switch: str
    static_lib_extension: str
    static_lib_format: str
    module_dir_switch: str
    module_include_switch: str
    ar_exe: str
    fc_exe: str
    executables: Any
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_debug(self): ...

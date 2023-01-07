from numpy.distutils.fcompiler import FCompiler as FCompiler
from typing import Any

compilers: Any

class LaheyFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    executables: Any
    module_dir_switch: Any
    module_include_switch: Any
    def get_flags_opt(self): ...
    def get_flags_debug(self): ...
    def get_library_dirs(self): ...
    def get_libraries(self): ...

from numpy.distutils.fcompiler import FCompiler as FCompiler
from typing import Any

compilers: Any

class FujitsuFCompiler(FCompiler):
    compiler_type: str
    description: str
    possible_executables: Any
    version_pattern: str
    executables: Any
    pic_flags: Any
    module_dir_switch: str
    module_include_switch: str
    def get_flags_opt(self): ...
    def get_flags_debug(self): ...
    def runtime_library_dir_option(self, dir): ...
    def get_libraries(self): ...

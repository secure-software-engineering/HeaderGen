from numpy.distutils.cpuinfo import cpu as cpu
from numpy.distutils.fcompiler import FCompiler as FCompiler
from typing import Any

compilers: Any

class MIPSFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    executables: Any
    module_dir_switch: Any
    module_include_switch: Any
    pic_flags: Any
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_arch_f77(self): ...
    def get_flags_arch_f90(self): ...

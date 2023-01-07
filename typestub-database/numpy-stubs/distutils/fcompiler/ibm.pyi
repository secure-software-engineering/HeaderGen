from numpy.distutils.exec_command import find_executable as find_executable
from numpy.distutils.fcompiler import FCompiler as FCompiler
from numpy.distutils.misc_util import make_temp_file as make_temp_file
from typing import Any

compilers: Any

class IBMFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    executables: Any
    version: Any
    def get_version(self, *args, **kwds): ...
    def get_flags(self): ...
    def get_flags_debug(self): ...
    def get_flags_linker_so(self): ...
    def get_flags_opt(self): ...

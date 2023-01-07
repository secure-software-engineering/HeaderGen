from numpy.distutils.fcompiler.gnu import GnuFCompiler as GnuFCompiler
from typing import Any

compilers: Any

class VastFCompiler(GnuFCompiler):
    compiler_type: str
    compiler_aliases: Any
    description: str
    version_pattern: str
    object_switch: str
    executables: Any
    module_dir_switch: Any
    module_include_switch: Any
    def find_executables(self) -> None: ...
    def get_version_cmd(self): ...
    version: Any
    def get_flags_arch(self): ...

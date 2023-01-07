from distutils.unixccompiler import UnixCCompiler
from numpy.distutils.ccompiler import simple_version_match as simple_version_match
from numpy.distutils.exec_command import find_executable as find_executable
from numpy.distutils.msvc9compiler import MSVCCompiler as MSVCCompiler
from typing import Any

class IntelCCompiler(UnixCCompiler):
    compiler_type: str
    cc_exe: str
    cc_args: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...

class IntelItaniumCCompiler(IntelCCompiler):
    compiler_type: str

class IntelEM64TCCompiler(UnixCCompiler):
    compiler_type: str
    cc_exe: str
    cc_args: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...

class IntelCCompilerW(MSVCCompiler):
    compiler_type: str
    compiler_cxx: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    cc: Any
    lib: Any
    linker: Any
    compile_options: Any
    compile_options_debug: Any
    def initialize(self, plat_name: Any | None = ...) -> None: ...

class IntelEM64TCCompilerW(IntelCCompilerW):
    compiler_type: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...

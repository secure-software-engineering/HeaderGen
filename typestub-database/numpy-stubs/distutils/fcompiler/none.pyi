from numpy.distutils import customized_fcompiler as customized_fcompiler
from numpy.distutils.fcompiler import FCompiler as FCompiler
from typing import Any

compilers: Any

class NoneFCompiler(FCompiler):
    compiler_type: str
    description: str
    executables: Any
    def find_executables(self) -> None: ...

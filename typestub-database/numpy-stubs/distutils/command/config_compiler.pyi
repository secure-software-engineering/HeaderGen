from distutils.core import Command
from numpy.distutils import log as log
from typing import Any

def show_fortran_compilers(_cache: Any | None = ...) -> None: ...

class config_fc(Command):
    description: str
    user_options: Any
    help_options: Any
    boolean_options: Any
    fcompiler: Any
    f77exec: Any
    f90exec: Any
    f77flags: Any
    f90flags: Any
    opt: Any
    arch: Any
    debug: Any
    noopt: Any
    noarch: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

class config_cc(Command):
    description: str
    user_options: Any
    compiler: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

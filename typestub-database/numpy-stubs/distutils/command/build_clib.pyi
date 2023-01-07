from distutils.command.build_clib import build_clib as old_build_clib
from numpy.distutils import log as log
from numpy.distutils.ccompiler_opt import new_ccompiler_opt as new_ccompiler_opt
from numpy.distutils.misc_util import filter_sources as filter_sources, get_lib_source_files as get_lib_source_files, get_numpy_include_dirs as get_numpy_include_dirs, has_cxx_sources as has_cxx_sources, has_f_sources as has_f_sources, is_sequence as is_sequence
from typing import Any

class build_clib(old_build_clib):
    description: str
    user_options: Any
    boolean_options: Any
    fcompiler: Any
    inplace: int
    parallel: Any
    warn_error: Any
    cpu_baseline: Any
    cpu_dispatch: Any
    disable_optimization: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def have_f_sources(self): ...
    def have_cxx_sources(self): ...
    compiler: Any
    libraries: Any
    compiler_opt: Any
    def run(self) -> None: ...
    def get_source_files(self): ...
    def build_libraries(self, libraries) -> None: ...
    def build_a_library(self, build_info, lib_name, libraries) -> None: ...

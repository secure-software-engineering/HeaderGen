from distutils.errors import DistutilsError
from typing import Any

class NotFoundError(DistutilsError): ...
class AliasedOptionError(DistutilsError): ...
class AtlasNotFoundError(NotFoundError): ...
class FlameNotFoundError(NotFoundError): ...
class LapackNotFoundError(NotFoundError): ...
class LapackSrcNotFoundError(LapackNotFoundError): ...
class LapackILP64NotFoundError(NotFoundError): ...
class BlasOptNotFoundError(NotFoundError): ...
class BlasNotFoundError(NotFoundError): ...
class BlasILP64NotFoundError(NotFoundError): ...
class BlasSrcNotFoundError(BlasNotFoundError): ...
class FFTWNotFoundError(NotFoundError): ...
class DJBFFTNotFoundError(NotFoundError): ...
class NumericNotFoundError(NotFoundError): ...
class X11NotFoundError(NotFoundError): ...
class UmfpackNotFoundError(NotFoundError): ...

class system_info:
    dir_env_var: Any
    search_static_first: int
    section: str
    saved_results: Any
    notfounderror: Any
    local_prefixes: Any
    cp: Any
    files: Any
    def __init__(self, default_lib_dirs=..., default_include_dirs=...) -> None: ...
    def parse_config_files(self) -> None: ...
    def calc_libraries_info(self): ...
    def set_info(self, **info) -> None: ...
    def get_option_single(self, *options): ...
    def has_info(self): ...
    def calc_extra_info(self): ...
    def get_info(self, notfound_action: int = ...): ...
    def get_paths(self, section, key): ...
    def get_lib_dirs(self, key: str = ...): ...
    def get_runtime_lib_dirs(self, key: str = ...): ...
    def get_include_dirs(self, key: str = ...): ...
    def get_src_dirs(self, key: str = ...): ...
    def get_libs(self, key, default): ...
    def get_libraries(self, key: str = ...): ...
    def library_extensions(self): ...
    def check_libs(self, lib_dirs, libs, opt_libs=...): ...
    def check_libs2(self, lib_dirs, libs, opt_libs=...): ...
    def combine_paths(self, *args): ...

class fft_opt_info(system_info):
    def calc_info(self) -> None: ...

class fftw_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    ver_info: Any
    def calc_ver_info(self, ver_param): ...
    def calc_info(self) -> None: ...

class fftw2_info(fftw_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    ver_info: Any

class fftw3_info(fftw_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    ver_info: Any

class dfftw_info(fftw_info):
    section: str
    dir_env_var: str
    ver_info: Any

class sfftw_info(fftw_info):
    section: str
    dir_env_var: str
    ver_info: Any

class fftw_threads_info(fftw_info):
    section: str
    dir_env_var: str
    ver_info: Any

class dfftw_threads_info(fftw_info):
    section: str
    dir_env_var: str
    ver_info: Any

class sfftw_threads_info(fftw_info):
    section: str
    dir_env_var: str
    ver_info: Any

class djbfft_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class mkl_info(system_info):
    section: str
    dir_env_var: str
    def get_mkl_rootdir(self): ...
    def __init__(self) -> None: ...
    def calc_info(self) -> None: ...

class lapack_mkl_info(mkl_info): ...
class blas_mkl_info(mkl_info): ...

class atlas_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class atlas_blas_info(atlas_info):
    def calc_info(self) -> None: ...

class atlas_threads_info(atlas_info):
    dir_env_var: Any

class atlas_blas_threads_info(atlas_blas_info):
    dir_env_var: Any

class lapack_atlas_info(atlas_info): ...
class lapack_atlas_threads_info(atlas_threads_info): ...
class atlas_3_10_info(atlas_info): ...

class atlas_3_10_blas_info(atlas_3_10_info):
    def calc_info(self) -> None: ...

class atlas_3_10_threads_info(atlas_3_10_info):
    dir_env_var: Any

class atlas_3_10_blas_threads_info(atlas_3_10_blas_info):
    dir_env_var: Any

class lapack_atlas_3_10_info(atlas_3_10_info): ...
class lapack_atlas_3_10_threads_info(atlas_3_10_threads_info): ...

class lapack_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def calc_info(self) -> None: ...

class lapack_src_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class lapack_opt_info(system_info):
    notfounderror: Any
    lapack_order: Any
    order_env_var_name: str
    def calc_info(self) -> None: ...

class _ilp64_opt_info_mixin:
    symbol_suffix: Any
    symbol_prefix: Any

class lapack_ilp64_opt_info(lapack_opt_info, _ilp64_opt_info_mixin):
    notfounderror: Any
    lapack_order: Any
    order_env_var_name: str

class lapack_ilp64_plain_opt_info(lapack_ilp64_opt_info):
    symbol_prefix: str
    symbol_suffix: str

class lapack64__opt_info(lapack_ilp64_opt_info):
    symbol_prefix: str
    symbol_suffix: str

class blas_opt_info(system_info):
    notfounderror: Any
    blas_order: Any
    order_env_var_name: str
    def calc_info(self) -> None: ...

class blas_ilp64_opt_info(blas_opt_info, _ilp64_opt_info_mixin):
    notfounderror: Any
    blas_order: Any
    order_env_var_name: str

class blas_ilp64_plain_opt_info(blas_ilp64_opt_info):
    symbol_prefix: str
    symbol_suffix: str

class blas64__opt_info(blas_ilp64_opt_info):
    symbol_prefix: str
    symbol_suffix: str

class cblas_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any

class blas_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def calc_info(self) -> None: ...
    def get_cblas_libs(self, info): ...

class openblas_info(blas_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    @property
    def symbol_prefix(self): ...
    @property
    def symbol_suffix(self): ...
    def calc_info(self) -> None: ...
    def check_msvc_gfortran_libs(self, library_dirs, libraries): ...
    def check_symbols(self, info): ...

class openblas_lapack_info(openblas_info):
    section: str
    dir_env_var: str
    notfounderror: Any

class openblas_clapack_info(openblas_lapack_info): ...

class openblas_ilp64_info(openblas_info):
    section: str
    dir_env_var: str
    notfounderror: Any

class openblas_ilp64_lapack_info(openblas_ilp64_info): ...

class openblas64__info(openblas_ilp64_info):
    section: str
    dir_env_var: str
    symbol_suffix: str
    symbol_prefix: str

class openblas64__lapack_info(openblas_ilp64_lapack_info, openblas64__info): ...

class blis_info(blas_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def calc_info(self) -> None: ...

class flame_info(system_info):
    section: str
    notfounderror: Any
    def check_embedded_lapack(self, info): ...
    def calc_info(self) -> None: ...

class accelerate_info(system_info):
    section: str
    notfounderror: Any
    def calc_info(self) -> None: ...

class blas_src_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class x11_info(system_info):
    section: str
    notfounderror: Any
    def __init__(self) -> None: ...
    def calc_info(self) -> None: ...

class _numpy_info(system_info):
    section: str
    modulename: str
    notfounderror: Any
    def __init__(self) -> None: ...
    def calc_info(self) -> None: ...

class numarray_info(_numpy_info):
    section: str
    modulename: str

class Numeric_info(_numpy_info):
    section: str
    modulename: str

class numpy_info(_numpy_info):
    section: str
    modulename: str

class numerix_info(system_info):
    section: str
    def calc_info(self) -> None: ...

class f2py_info(system_info):
    def calc_info(self) -> None: ...

class boost_python_info(system_info):
    section: str
    dir_env_var: str
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class agg2_info(system_info):
    section: str
    dir_env_var: str
    def get_paths(self, section, key): ...
    def calc_info(self) -> None: ...

class _pkg_config_info(system_info):
    section: Any
    config_env_var: str
    default_config_exe: str
    append_config_exe: str
    version_macro_name: Any
    release_macro_name: Any
    version_flag: str
    cflags_flag: str
    def get_config_exe(self): ...
    def get_config_output(self, config_exe, option): ...
    def calc_info(self) -> None: ...

class wx_info(_pkg_config_info):
    section: str
    config_env_var: str
    default_config_exe: str
    append_config_exe: str
    version_macro_name: str
    release_macro_name: str
    version_flag: str
    cflags_flag: str

class gdk_pixbuf_xlib_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gdk_pixbuf_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gdk_x11_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gdk_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gdk_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gtkp_x11_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class gtkp_2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class xft_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class freetype2_info(_pkg_config_info):
    section: str
    append_config_exe: str
    version_macro_name: str

class amd_info(system_info):
    section: str
    dir_env_var: str
    def calc_info(self) -> None: ...

class umfpack_info(system_info):
    section: str
    dir_env_var: str
    notfounderror: Any
    def calc_info(self) -> None: ...

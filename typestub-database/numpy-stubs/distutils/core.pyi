from numpy.distutils.command import bdist_rpm as bdist_rpm, build as build, build_clib as build_clib, build_ext as build_ext, build_py as build_py, build_scripts as build_scripts, build_src as build_src, config as config, config_compiler as config_compiler, develop as develop, egg_info as egg_info, install as install, install_clib as install_clib, install_data as install_data, install_headers as install_headers, sdist as sdist
from numpy.distutils.extension import Extension as Extension
from numpy.distutils.misc_util import is_sequence as is_sequence, is_string as is_string
from numpy.distutils.numpy_distribution import NumpyDistribution as NumpyDistribution
from typing import Any

have_setuptools: bool
numpy_cmdclass: Any

def get_distribution(always: bool = ...): ...
def setup(**attr): ...

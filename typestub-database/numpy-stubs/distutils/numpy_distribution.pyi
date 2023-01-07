from distutils.core import Distribution
from typing import Any

class NumpyDistribution(Distribution):
    scons_data: Any
    installed_libraries: Any
    installed_pkg_config: Any
    def __init__(self, attrs: Any | None = ...) -> None: ...
    def has_scons_scripts(self): ...

from distutils.command.build_scripts import build_scripts as old_build_scripts
from numpy.distutils import log as log
from numpy.distutils.misc_util import is_string as is_string
from typing import Any

class build_scripts(old_build_scripts):
    def generate_scripts(self, scripts): ...
    scripts: Any
    def run(self): ...
    def get_source_files(self): ...

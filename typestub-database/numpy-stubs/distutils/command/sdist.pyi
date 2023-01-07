from distutils.command.sdist import sdist as old_sdist
from numpy.distutils.misc_util import get_data_files as get_data_files

class sdist(old_sdist):
    def add_defaults(self) -> None: ...

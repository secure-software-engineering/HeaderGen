from distutils.command.install_data import install_data as old_install_data
from typing import Any

have_setuptools: Any

class install_data(old_install_data):
    def run(self) -> None: ...
    def finalize_options(self) -> None: ...

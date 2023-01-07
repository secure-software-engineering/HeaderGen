from setuptools.command.develop import develop as old_develop
from typing import Any

class develop(old_develop):
    __doc__: Any
    def install_for_development(self) -> None: ...

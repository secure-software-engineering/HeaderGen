from typing import Any

have_setuptools: bool
old_install: Any

class install(old_install):
    sub_commands: Any
    install_lib: Any
    def finalize_options(self) -> None: ...
    def setuptools_run(self): ...
    def run(self): ...

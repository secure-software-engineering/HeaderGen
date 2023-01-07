import typing as t
from mypy.nodes import MypyFile as MypyFile, Statement as Statement
from mypy.plugin import Plugin

MYPY_EX: t.Optional[ModuleNotFoundError]

class _NumpyPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str) -> t.Optional[_HookFunc]: ...
    def get_additional_deps(self, file: MypyFile) -> t.List[t.Tuple[int, str, int]]: ...

def plugin(version: str) -> t.Type[_NumpyPlugin]: ...

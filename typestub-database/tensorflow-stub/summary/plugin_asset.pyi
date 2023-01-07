import abc
from tensorflow.python.framework import ops as ops
from typing import Any

def get_plugin_asset(plugin_asset_cls, graph: Any | None = ...): ...
def get_all_plugin_assets(graph: Any | None = ...): ...

class PluginAsset(metaclass=abc.ABCMeta):
    plugin_name: Any
    @abc.abstractmethod
    def assets(self): ...

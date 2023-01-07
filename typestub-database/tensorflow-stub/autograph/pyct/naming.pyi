from tensorflow.python.autograph.pyct import qual_names as qual_names
from typing import Any

class Namer:
    global_namespace: Any
    generated_names: Any
    def __init__(self, global_namespace) -> None: ...
    def new_symbol(self, name_root, reserved_locals): ...

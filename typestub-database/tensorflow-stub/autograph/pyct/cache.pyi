class _TransformedFnCache:
    def __init__(self) -> None: ...
    def has(self, entity, subkey): ...
    def __getitem__(self, entity): ...
    def __len__(self): ...

class CodeObjectCache(_TransformedFnCache): ...
class UnboundInstanceCache(_TransformedFnCache): ...

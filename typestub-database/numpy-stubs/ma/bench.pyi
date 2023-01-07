from typing import Any

xs: Any
ys: Any
zs: Any
m1: Any
m2: Any
nmxs: Any
nmys: Any
nmzs: Any
xl: Any
yl: Any
zl: Any
maskx: Any
masky: Any
nmxl: Any
nmyl: Any
nmzl: Any

def timer(s, v: str = ..., nloop: int = ..., nrep: int = ...) -> None: ...
def compare_functions_1v(func, nloop: int = ..., xs=..., nmxs=..., xl=..., nmxl=...) -> None: ...
def compare_methods(methodname, args, vars: str = ..., nloop: int = ..., test: bool = ..., xs=..., nmxs=..., xl=..., nmxl=...) -> None: ...
def compare_functions_2v(func, nloop: int = ..., test: bool = ..., xs=..., nmxs=..., ys=..., nmys=..., xl=..., nmxl=..., yl=..., nmyl=...) -> None: ...

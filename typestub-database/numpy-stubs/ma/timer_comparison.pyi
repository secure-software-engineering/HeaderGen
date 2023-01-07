from numpy import float_ as float_
from numpy.testing import build_err_msg as build_err_msg
from typing import Any

pi: Any

class ModuleTester:
    module: Any
    allequal: Any
    arange: Any
    array: Any
    concatenate: Any
    count: Any
    equal: Any
    filled: Any
    getmask: Any
    getmaskarray: Any
    id: Any
    inner: Any
    make_mask: Any
    masked: Any
    masked_array: Any
    masked_values: Any
    mask_or: Any
    nomask: Any
    ones: Any
    outer: Any
    repeat: Any
    resize: Any
    sort: Any
    take: Any
    transpose: Any
    zeros: Any
    MaskType: Any
    umath: Any
    testnames: Any
    def __init__(self, module) -> None: ...
    def assert_array_compare(self, comparison, x, y, err_msg: str = ..., header: str = ..., fill_value: bool = ...) -> None: ...
    def assert_array_equal(self, x, y, err_msg: str = ...) -> None: ...
    def test_0(self) -> None: ...
    def test_1(self): ...
    def test_2(self) -> None: ...
    def test_3(self) -> None: ...
    def test_4(self) -> None: ...
    def test_5(self) -> None: ...
    def test_6(self) -> None: ...
    def test_7(self) -> None: ...
    def test_99(self) -> None: ...
    def test_A(self) -> None: ...

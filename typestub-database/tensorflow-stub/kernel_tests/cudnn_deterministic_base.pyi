from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, test_util as test_util
from tensorflow.python.ops import nn_ops as nn_ops
from tensorflow.python.platform import test as test
from typing import Any, NamedTuple

class LayerShapeNHWC(NamedTuple):
    batch: Any
    height: Any
    width: Any
    channels: Any

class FilterShape2D(NamedTuple):
    height: Any
    width: Any
    in_channels: Any
    out_channels: Any

class LayerShapeNCDHW(NamedTuple):
    batch: Any
    channels: Any
    depth: Any
    height: Any
    width: Any

class FilterShape3D(NamedTuple):
    depth: Any
    height: Any
    width: Any
    in_channels: Any
    out_channels: Any

class ConvolutionTest(test.TestCase):
    def testForward(self) -> None: ...
    def testBackwardFilterGradient(self) -> None: ...
    def testBackwardInputGradient(self) -> None: ...

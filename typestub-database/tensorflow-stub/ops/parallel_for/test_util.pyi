from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import test as test
from tensorflow.python.util import nest as nest

class PForTestCase(test.TestCase):
    def run_and_assert_equal(self, targets1, targets2, rtol: float = ..., atol: float = ...) -> None: ...

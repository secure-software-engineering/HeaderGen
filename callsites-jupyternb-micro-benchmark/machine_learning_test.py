
import os

from base import TestBase

class MachineLearningTest(TestBase):
    snippet_dir = "machine_learning"

    def test_return_type(self):
        self.validate_snippet(self.get_snippet_path("return_type"))

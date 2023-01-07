
import os

from base import TestBase

class TaskTestTest(TestBase):
    snippet_dir = "task_test"

    def test_custom(self):
        self.validate_snippet(self.get_snippet_path("custom"))

    def test_expanded(self):
        self.validate_snippet(self.get_snippet_path("expanded"))

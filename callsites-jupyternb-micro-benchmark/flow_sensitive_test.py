
import os

from base import TestBase

class FlowSensitiveTest(TestBase):
    snippet_dir = "flow_sensitive"

    def test_conditional(self):
        self.validate_snippet(self.get_snippet_path("conditional"))

    def test_multiple_class(self):
        self.validate_snippet(self.get_snippet_path("multiple_class"))

    def test_multiple_func(self):
        self.validate_snippet(self.get_snippet_path("multiple_func"))

    def test_multi_assign_per_line(self):
        self.validate_snippet(self.get_snippet_path("multi_assign_per_line"))

    def test_reassigned_call(self):
        self.validate_snippet(self.get_snippet_path("reassigned_call"))

    def test_repeated(self):
        self.validate_snippet(self.get_snippet_path("repeated"))

    def test_simple(self):
        self.validate_snippet(self.get_snippet_path("simple"))

    def test_tuples(self):
        self.validate_snippet(self.get_snippet_path("tuples"))

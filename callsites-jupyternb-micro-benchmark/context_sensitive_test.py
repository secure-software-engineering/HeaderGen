
import os

from base import TestBase

class ContextSensitiveTest(TestBase):
    snippet_dir = "context_sensitive"

    def test_attribute(self):
        self.validate_snippet(self.get_snippet_path("attribute"))

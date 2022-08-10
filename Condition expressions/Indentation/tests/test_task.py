import unittest


class TestCase(unittest.TestCase):
    def test_indent(self):
        try:
            import indentation

        except IndentationError as e:
            self.fail(msg=f"Fix the code! IndentationError was raised: {e}")

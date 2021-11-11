import unittest


class TestCase(unittest.TestCase):
    def test_true(self):
        try:
            from in_operator import contains
            self.assertTrue(contains is True, msg="Are you sure that ice cream does not contain ice?")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

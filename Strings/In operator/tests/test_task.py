import unittest

try:
    from in_operator import contains

    class TestCase(unittest.TestCase):
        def test_true(self):
            self.assertTrue(contains is True, msg="Are you sure that ice cream does not contain ice?")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")

import unittest

try:
    from negative_indexing import long_string, exclamation

    class TestCase(unittest.TestCase):
        def test_add(self):
            self.assertEqual(exclamation, long_string[-1], msg="Make sure you get the last symbol of the long_string.")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")

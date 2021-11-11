import unittest


class TestCase(unittest.TestCase):
    def test_add(self):
        try:
            from negative_indexing import long_string, exclamation
            self.assertEqual(exclamation, long_string[-1], msg="Make sure you get the last symbol of the long_string.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

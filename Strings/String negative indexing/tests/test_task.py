import unittest


class TestCase(unittest.TestCase):
    def test_add(self):
        try:
            from negative_indexing import long_string, exclamation
            self.assertEqual(long_string[-1], exclamation, msg="Make sure you get the last symbol of long_string.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

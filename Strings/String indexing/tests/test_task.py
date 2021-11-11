import unittest


class TestCase(unittest.TestCase):
    def test_indexing(self):
        try:
            from string_indexing import python, p_letter
            self.assertEqual(python[0], p_letter, msg="Make sure you get the first letter from the word Python.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")




import unittest


class TestCase(unittest.TestCase):
    def test_indexing(self):
        try:
            from string_indexing import python, p_letter
            self.assertEqual(p_letter, python[0], msg="Make sure you get the first letter from the word Python.")

        except ImportError:
            self.assertEqual(1, 2, msg="Do not rename any variables.")




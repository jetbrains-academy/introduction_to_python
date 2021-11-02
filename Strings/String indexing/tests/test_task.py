import unittest

try:
    from string_indexing import python, p_letter

    class TestCase(unittest.TestCase):
        def test_add(self):
            self.assertEqual(p_letter, python[0], msg="Make sure you get the first letter from the word Python.")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")




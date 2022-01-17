import unittest

try:
    from slicing import monty_python, python

    class TestCase(unittest.TestCase):
        def test_string(self):
            self.assertEqual(monty_python[6:], python,  msg="Wrong string result.")

        def test_space(self):
            self.assertFalse(' ' in python, msg="Do not include the space in the result string.")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Do not rename any variables.")

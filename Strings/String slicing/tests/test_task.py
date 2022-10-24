import unittest

try:
    from slicing import monty_python, python

    class TestCase(unittest.TestCase):
        def test_string(self):
            self.assertEqual(monty_python[6:], python,  msg="Wrong string result.")

        def test_space(self):
            self.assertFalse(' ' in python, msg="Do not include the space in the result string.")

        def test_0_code_len(self):
            with open("slicing.py", "r") as taskfile:
                lines = taskfile.readlines()
                self.assertTrue(len(lines) == 6, msg="Please do not add or remove any lines from the code file.")

        def test_statement_1(self):
            with open("slicing.py", "r") as taskfile:
                lines = taskfile.readlines()
                code = lines[-2]
                if not ("[6:]" in code):
                    self.fail(msg="Your solution does not use string slicing.")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Do not rename any variables.")


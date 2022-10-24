import unittest


class TestCase(unittest.TestCase):
    def test_import_hello(self):
        try:
            from concatenation import hello_world
            self.assertEqual('Hello World', hello_world, msg="Wrong string result.")
            self.assertTrue(' ' in hello_world, msg='The string result should contain a space.')

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

    def test_0_code_len(self):
        with open("concatenation.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 5, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("concatenation.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            self.assertTrue("+" in code, msg="Your solution does not use concatenation.")
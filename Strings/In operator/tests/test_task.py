import unittest


class TestCase(unittest.TestCase):
    def test_true(self):
        try:
            from in_operator import contains
            self.assertTrue(contains is True, msg="Are you sure that ice cream does not contain ice?")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

    def test_0_code_len(self):
        with open("in_operator.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 5, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("in_operator.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("in" in code):
                self.fail(msg="Your solution does not use the in operator.")
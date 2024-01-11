import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    from task import *
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual('9', output[0], msg='The second printed element should be 9.')
        self.assertEqual('10', output[1], msg='The second printed element should be 10.')

    def test_0_code_len(self):
        with open("task.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 4, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("task.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("my_list[2][2]" in code):
                self.fail(msg="Your solution should use indexing.")

    def test_statement_2(self):
        with open("task.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1]
            if not ("my_list[3]" in code):
                self.fail(msg="Your solution should use indexing.")

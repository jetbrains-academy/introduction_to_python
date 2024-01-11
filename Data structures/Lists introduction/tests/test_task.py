import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from lists import squares
output = f.getvalue().split('\n')
result_str = output[1]
correct_string = str(squares[1:4])  # [4, 9, 16]


class TestCase(unittest.TestCase):
    def test_slice(self):
        self.assertEqual(correct_string, result_str, msg='The resulting slice does not match the expected one.')

    def test_0_code_len(self):
        with open("lists.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 4, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("lists.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1]
            if not ("squares[1:4]" in code):
                self.fail(msg="Your solution should use slicing.")
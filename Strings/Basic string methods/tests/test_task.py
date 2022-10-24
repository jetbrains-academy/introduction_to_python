import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    import string_methods
output = f.getvalue().split('\n')
result_str = output[2]
correct_string = 'MONTY PYTHON'


class TestCase(unittest.TestCase):
    def test_out_len(self):
        self.assertEqual(4, len(output), msg='Do not remove or add any print statements.')

    def test_string(self):
        self.assertEqual(correct_string, result_str, msg='Wrong result string.')

    def test_0_code_len(self):
        with open("string_methods.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 6, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("string_methods.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1]
            if not (".upper()" in code):
                self.fail(msg="Your solution should use the function .upper().")

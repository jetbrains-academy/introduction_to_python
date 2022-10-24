import unittest
import contextlib
import io

f = io.StringIO()
with contextlib.redirect_stdout(f):
    import boolean_operators
output = f.getvalue().split('\n')
result = output[1]


class TestCase(unittest.TestCase):
    def test_out_len(self):
        self.assertEqual(3, len(output), msg='Please do not remove or add any print statements.')

    def test_out_str(self):
        self.assertEqual('True', result, msg='Your expression does not seem to produce the correct result.')


    def test_0_code_len(self):
        with open("boolean_operators.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 6, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("boolean_operators.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1]
            if not ('==' in code and "and" in code and ">=" in code):
                self.fail(msg="Your solution should evaluate the variables name and age.")
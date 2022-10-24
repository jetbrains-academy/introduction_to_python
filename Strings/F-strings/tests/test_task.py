import contextlib
import io
import unittest
import re

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from f_strings import name, age
output = f.getvalue().split('\n')
result_str = output[0]
correct_string = f"Hello, My name is {name} and I'm {age} years old."


class TestCase(unittest.TestCase):
    def test_out_len(self):
        self.assertEqual(2, len(output), msg='Do not remove or add any print statements.')

    def test_name(self):
        self.assertTrue(type(name) == str, msg='Your name should be a string.')

    def test_string_age(self):
        self.assertIsNotNone(re.search(r'\d+', result_str), msg='The resulting string should contain '
                                                               'your age written in digits.')

    def test_age(self):
        self.assertIsNotNone(re.match(r'\d+', str(age)), msg='`age` should contain only digits')

    def test_string(self):
        self.assertIsNotNone(re.match(correct_string, result_str), msg='The result string does not match the expected one.')

    def test_0_code_len(self):
        with open("f_strings.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 3, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("f_strings.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1]
            if not ("{name}" in code and "{age}" in code):
                self.fail(msg="Your solution should use f-string syntax.")




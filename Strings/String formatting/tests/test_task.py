import contextlib
import io
import unittest
import re

f = io.StringIO()
with contextlib.redirect_stdout(f):
    import string_formatting
output = f.getvalue().split('\n')
result_str = output[1]
correct_string = "I'm \d+ years old"


class TestCase(unittest.TestCase):
    def test_out_len(self):
        self.assertEqual(3, len(output), msg='Do not remove or add any print statements.')

    def test_string(self):
        self.assertIsNotNone(re.match(correct_string, result_str), msg='The result string does not match the expected.')

    def test_string_age(self):
        self.assertIsNotNone(re.search(r'\d+', result_str), msg='The result string does not contain your age.')




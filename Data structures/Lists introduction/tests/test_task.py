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
        self.assertEqual(result_str, correct_string, msg='The resulting slice does not match the expected.')


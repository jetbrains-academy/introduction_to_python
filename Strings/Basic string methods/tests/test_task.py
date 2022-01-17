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

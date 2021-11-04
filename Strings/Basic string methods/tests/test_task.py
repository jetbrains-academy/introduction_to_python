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
    def test_string(self):
        self.assertEqual(result_str, correct_string, msg='Wrong result string.')

    def test_out_len(self):
        self.assertEqual(len(output), 4, msg='Do not remove or add any print statements.')



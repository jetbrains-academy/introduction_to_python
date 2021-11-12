import unittest
import contextlib
import io

f = io.StringIO()
with contextlib.redirect_stdout(f):
    import boolean_order
output = f.getvalue().split('\n')
result = output[2]


class TestCase(unittest.TestCase):
    def test_out_len(self):
        self.assertEqual(4, len(output), msg='Please do not remove or add any print statements.')

    def test_out_str(self):
        self.assertEqual('True', result, msg='Your expression does not seem to produce the correct result.')
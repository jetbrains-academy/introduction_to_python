import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from tuples import my_tuple
output = f.getvalue().split('\n')
result_1 = output[0]
result_2 = output[1]


class TestCase(unittest.TestCase):
    def test_len(self):
        self.assertEqual(str(26), result_1, msg='Are you sure you got the correct alphabet length?')

    def test_tuple(self):
        self.assertTrue(type(my_tuple) == tuple, msg='my_tuple should be a tuple!')


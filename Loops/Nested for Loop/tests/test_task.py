import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    from task import *
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_list(self):
        expected_output = ['1 x 1', '1 x 2', '1 x 3', '2 x 1', '2 x 2', '2 x 3', '3 x 1', '3 x 2', '3 x 3', '']
        self.assertEqual(expected_output, output, msg='Your result does not match the expected.')

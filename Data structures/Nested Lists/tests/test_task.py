import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    from task import *
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual('9', output[0], msg='The second printed element should be 9.')
        self.assertEqual('10', output[1], msg='The second printed element should be 10.')

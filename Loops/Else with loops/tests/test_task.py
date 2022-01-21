import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    from else_with_loops import *
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_default(self):
        default_out = ["it's less than 5", "it's less than 5",
                       "it's less than 5", "it's less than 5",
                       "it's less than 5", "and now it's 5", '1',
                       '2', '3', '4', 'for loop is done', 'Outside the for loop', '']
        self.assertNotEqual(default_out, output, msg='You need to add a correct condition and a break statement.')

    def test_correct(self):
        if len(output) == 13:
            self.test_default()
        expected = ["it's less than 5", "it's less than 5", "it's less than 5",
                   "it's less than 5", "it's less than 5", "and now it's 5",
                   '1', '2', 'Outside the for loop', '']
        self.assertEqual(expected, output, msg='Your code does not print what is expected. Check your condition. '
                                              'Please do not change the starter code.')


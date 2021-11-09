import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    from continue_keyword import *
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_default(self):
        correct = ['0', '1', '2', '4', '1', '3', '5', '7', '9', '']
        self.assertEqual(correct, output, msg='Wrong output. Check your condition. Please do not change the '
                                              'starter code.')

    def test_condition(self):
        incorrect = ['0', '1', '2', '4', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']
        self.assertNotEqual(incorrect, output, msg='You need to add a condition and a keyword to skip even numbers.')


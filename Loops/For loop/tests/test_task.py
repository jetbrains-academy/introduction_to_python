import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from for_loop import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_loop(self):
            self.assertEqual('0', output[0], msg='Please do not change the starter code.')
            self.assertEqual('1', output[1], msg='Please do not change the starter code.')
            self.assertEqual('2', output[2], msg='Please do not change the starter code.')
            self.assertEqual('3', output[3], msg='Please do not change the starter code.')
            self.assertEqual('4', output[4], msg='Please do not change the starter code.')
            self.assertEqual('2', output[5], msg='Your code does not print the `primes`')
            self.assertEqual('3', output[6], msg='Your code does not print the `primes`')
            self.assertEqual('5', output[7], msg='Your code does not print the `primes`')
            self.assertEqual('7', output[8], msg='Your code does not print the `primes`')
            self.assertEqual(['0', '1', '2', '3', '4', '2', '3', '5', '7', ''], output, msg='Wrong output.')

except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add a for statement before the last print statement.')
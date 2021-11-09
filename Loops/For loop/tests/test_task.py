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
            self.assertEqual(output[0], '0', msg='Please do not change the starter code.')
            self.assertEqual(output[1], '1', msg='Please do not change the starter code.')
            self.assertEqual(output[2], '2', msg='Please do not change the starter code.')
            self.assertEqual(output[3], '3', msg='Please do not change the starter code.')
            self.assertEqual(output[4], '4', msg='Please do not change the starter code.')
            self.assertEqual(output[5], '2', msg='Your code does not print the `primes`')
            self.assertEqual(output[6], '3', msg='Your code does not print the `primes`')
            self.assertEqual(output[7], '5', msg='Your code does not print the `primes`')
            self.assertEqual(output[8], '7', msg='Your code does not print the `primes`')
            self.assertEqual(output, ['0', '1', '2', '3', '4', '2', '3', '5', '7', ''], msg='Wrong output.')

except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add a for statement before the last print statement.')
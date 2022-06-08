import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from order import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_table(self):
            self.assertEqual('|____|____|____|____|____|', output[0], msg='The table should have 5 columns.')
            self.assertEqual(11, len(output), msg='The table should have 5 rows.')


except SyntaxError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Positional argument should not follow keyword argument')
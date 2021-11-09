import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from for_string import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_loop(self):
            self.assertEqual(len(output), 15, msg='Wrong output length. Please do not change anything '
                                                  'in the starter code apart from the answer placeholder')
            self.assertEqual(output[-2], 'True', msg='`length` should be equal to `len(hello_world)`.')

except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add a for statement before length incrementation.')
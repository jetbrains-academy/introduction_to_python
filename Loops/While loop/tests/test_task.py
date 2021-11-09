import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from while_loop import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_finished(self):
            self.assertEqual(output[10], 'Finished', msg='Please do not change the starter code.')

        def test_output(self):
            self.assertEqual(output[11:20], ['1', '4', '9', '16', '25', '36', '49', '64', '81'],
                             msg='Your while loop does not output all of the needed squares.')

        def test_last(self):
            self.assertEqual(output[-2], '81', msg='The last square should be 81. Maybe check your while loop '
                                                   'condition.')

except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add a while statement with a condition.')

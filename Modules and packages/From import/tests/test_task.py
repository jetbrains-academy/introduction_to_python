import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        import from_import
    output = f.getvalue().split('\n')


    class TestCase(unittest.TestCase):
        def test_output(self):
            expected, actual = 'Hey there, User!', output[0]
            self.assertEqual(expected, actual,
                             msg='Please do not change the starter code.')
            expected, actual = '66.66666666666667', output[1]
            self.assertEqual(expected, actual,
                             msg='Calculation result is wrong. Please do not change the starter code.')

except NameError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Use `Calculator` directly, without a prefix.')




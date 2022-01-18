import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from break_keyword import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_loop(self):
            self.assertTrue(output[5] == 'python' and output[6] == 'giraffe' and output[7] == 'elephant' and output[8] != 'tiger',
                            msg='Your loop should only print the last three animals in reverse order.')

        def test_list(self):
            expected, actual = ['lion', 'tiger'], zoo
            self.assertEqual(expected, actual, msg='The zoo list in the end should contain only lion and tiger.')

except IndexError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add an if statement with a '
                                       'condition to exit the loop and a break statement after it.')

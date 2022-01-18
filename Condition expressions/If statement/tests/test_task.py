import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from if_statement import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_list(self):
            self.assertEqual([], tasks, msg='Do not change the tasks list.')

        def test_condition(self):
            self.assertEqual('Not an empty list!', output[2], msg='Your code should print "Not an empty list!" at first, because the list is not empty.')

        def test_condition2(self):
            self.assertEqual('Now empty!', output[3], msg='Your code should print "Now empty!" in the end, because the list is now empty.')

        def test_out_len(self):
            self.assertEqual(5, len(output), msg='Output should contain 4 lines.')


except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add an if statement with a condition before the last print statement.')




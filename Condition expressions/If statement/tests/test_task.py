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
            self.assertEqual(["task1", "task2"], tasks, msg='Do not change the tasks list.')

        def test_condition(self):
            self.assertNotEqual('empty list', output[2], msg='Your code prints "empty list", but the list is not empty.')

        def test_out_len(self):
            self.assertEqual(3, len(output), msg='Please do not remove or add any print statements.')


except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add an if statement with a condition before the last print statement.')




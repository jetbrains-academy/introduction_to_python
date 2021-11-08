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
            self.assertEqual(tasks, ["task1", "task2"], msg='Do not change the tasks list.')

        def test_condition(self):
            self.assertNotEqual(output[2], 'empty list', msg='Your code prints "empty list", but the list is not empty.')

        def test_out_len(self):
            self.assertEqual(len(output), 3, msg='Please do not remove or add any print statements.')


except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add an if statement with a condition before the last print statement.')




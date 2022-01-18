import unittest
import contextlib
import io

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from else_elif import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_list(self):
            self.assertEqual('John', name, msg='Please do not change the value of the variable `name`.')

        def test_condition1(self):
            self.assertNotEqual('False', output[1], msg='You need to print True if name is "John"')

        def test_condition(self):
            self.assertEqual('True', output[1], msg='You need to print True if name is "John"')

        def test_out_len(self):
            self.assertEqual(3, len(output), msg='Please do not remove or add any print statements.')


except IndentationError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to add an if statement with a condition and an else statement.')




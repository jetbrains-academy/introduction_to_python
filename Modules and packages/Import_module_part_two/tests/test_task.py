import unittest
import contextlib
import io
import re
import calculator

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from imports import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_class(self):
            try:
                self.assertTrue(isinstance(calc, calculator.Calculator),
                                msg='`calc` should be an instance of Calculator.')
            except NameError:
                self.assertTrue(False, msg='Do not change variable names.')

        def test_out(self):
            expected, actual = str(4950), output[0]
            self.assertEqual(expected, actual, msg='Calculation result looks wrong.')

except NameError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to import the calculator module.')

except ModuleNotFoundError:
    class TestFailCase1(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Don't use file extensions in imports.")

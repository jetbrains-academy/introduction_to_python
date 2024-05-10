import unittest
import contextlib
import io
import re

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        from imports import *
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_out(self):
            expected, actual = 'Hello, World! My name is John', output[0]
            self.assertEqual(expected, actual, msg='Call hello_world with "John" argument')

except AttributeError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to use hello_world function from my_funcs module.')

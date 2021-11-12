import contextlib
import io
import unittest
import re

try:
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        from class_definition import MyClass, my_object
    output = f.getvalue().split('\n')


    class TestCase(unittest.TestCase):
        def test_class(self):
            self.assertTrue(isinstance(my_object, MyClass), msg='Object `my_object` has to be an instance of `MyClass`.')

        def test_out(self):
            expected, actual = str(my_object.variable), output[1]
            self.assertEqual(expected, actual, msg='Your code should print the value of the '
                                                                '`variable` attribute after it prints the '
                                                                '`foo` function message.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class and variable names.')




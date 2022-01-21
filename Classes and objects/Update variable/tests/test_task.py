import contextlib
import io
import unittest
import re

try:
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        from update_variable import Car, car1, car2
    output = f.getvalue().split('\n')


    class TestCase(unittest.TestCase):
        def test_instances(self):
            self.assertTrue(isinstance(car1, Car), msg='The object car1 has to be an instance of Car.')
            self.assertTrue(isinstance(car2, Car), msg='The object car2 has to be an instance of Car.')

        def test_out(self):
            expected, actual = car1.description(), output[0]
            self.assertEqual(expected, actual, msg='Please do not change the starter code.')
            expected, actual = car2.description(), output[1]
            self.assertEqual(expected, actual, msg='The second print statement should print the '
                                                                'description of car2, which should include '
                                                                'its `color`.')

        def test_method_call_syntax(self):
            self.assertFalse('<bound method ' in output[0], msg='To call a method properly, you need to use the syntax such as `object.method()`. '
                                                                'Without brackets, this will just return the function object.')
            self.assertFalse('<bound method ' in output[1], msg='To call a method properly, you need to use the syntax such as `object.method()`. '
                                                                'Without brackets, this will just return the function object.')


except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class and variable names.')




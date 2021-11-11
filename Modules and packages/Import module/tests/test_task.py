import unittest
import contextlib
import io
import re

f = io.StringIO()
try:
    with contextlib.redirect_stdout(f):
        import imports
    output = f.getvalue().split('\n')

    class TestCase(unittest.TestCase):
        def test_loop(self):
            self.assertEqual(output[0], '2', msg='Please do not change the starter code.')
            self.assertTrue(re.match(r'Hello, World! My name is \w+', output[1]),
                            msg='Your code should call `hello_world` function from `my_module` with some name '
                                'so that it prints the greeting.')

except NameError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='You need to import `my_module`.')

except ModuleNotFoundError:
    class TestFailCase1(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Don't use file extensions in imports.")

import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch
from sys import setrecursionlimit


def try_import():
    import recursion
    return recursion


class TestCase(unittest.TestCase):
    task_name = 'recursion'

    def setUp(self):
        try:
            # Stores output from print() in actualOutput
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                # Loads submission on first test, reloads on subsequent tests
                if self.task_name in sys.modules:
                    importlib.reload(sys.modules[self.task_name])
                else:
                    importlib.import_module(self.task_name)
        except NameError as ne:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_factorial_1(self):
        expected_factorial_10 = 3628800

        try:
            actual_factorial_function = try_import().factorial
        except AttributeError:
            self.fail(msg="There was a problem while importing the factorial function. "
                          "Make sure its signature remains intact.")

        actual_factorial_10 = actual_factorial_function(10)

        self.assertEqual(expected_factorial_10, actual_factorial_10, msg="The value returned for n = 10 "
                                                                         "seems to be incorrect. Check the function "
                                                                         "implementation.")

    def test_factorial_2(self):
        expected_factorial_12 = 479001600

        try:
            actual_factorial_function = try_import().factorial
        except AttributeError:
            self.fail(msg="There was a problem while importing the factorial function. "
                          "Make sure its signature remains intact.")

        actual_factorial_12 = actual_factorial_function(12)

        self.assertEqual(expected_factorial_12, actual_factorial_12, msg="The value returned for n = 12 "
                                                                         "seems to be incorrect. Check the function "
                                                                         "implementation.")

    def test_recursion(self):
        setrecursionlimit(1000)
        try:
            actual_factorial_function = try_import().factorial
        except AttributeError:
            self.fail(msg="There was a problem while importing the factorial function. "
                          "Make sure its signature remains intact.")

        with self.assertRaises(RecursionError,  msg="No recursion was detected in the"
                                                    " factorial function."):
            actual_factorial_function(1005)

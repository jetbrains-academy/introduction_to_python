import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import  return_keyword
    return  return_keyword


class TestCase(unittest.TestCase):
    task_name = 'return_keyword'

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
            self.fail("There was a problem while loading the solution - {0}. Check the solution for "
                      "IDE-highlighted  errors and warnings.".format(str(e)))

    def test_keyword_return(self):
        expected_fib_22_result = [1, 1, 2, 3, 5, 8, 13, 21]

        try:
            actual_fib = try_import().fib
        except AttributeError:
            self.fail(msg="There was a problem while loading fib function. Make sure its declaration stays intact.")

        actual_fib_22_result = actual_fib(22)

        self.assertEqual(expected_fib_22_result, actual_fib_22_result, msg="The Fibonacci sequence up to 22 is "
                                                                           "incorrect. Make sure you return the result "
                                                                           "needed.")

import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import arithmetic_operators
    return arithmetic_operators


class TestCase(unittest.TestCase):
    task_name = 'arithmetic_operators'
    # unittest.TestLoader.sortTestMethodsUsing =

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

    def test_ordered_4_addition(self):
        expected_addition_result = 22.5

        try:
            actual_addition_result = try_import().addition_result
        except AttributeError:
            self.fail(msg="The variable addition_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_addition_result, actual_addition_result, msg="Something does not ADD up.")

    def test_ordered_1_division(self):
        expected_division_result = 4.5

        try:
            actual_division_result = try_import().division_result
        except AttributeError:
            self.fail(msg="The variable division_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_division_result, actual_division_result, msg="The division result value seems to be "
                                                                               "a bit off.")


    def test_ordered_3_multiplication_result(self):
        expected_multiplication_result = 18.0

        try:
            actual_multiplication_result = try_import().multiplication_result
        except AttributeError:
            self.fail(msg="The variable multiplication_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_multiplication_result, actual_multiplication_result,
                         msg="The multiplication result value seems to be "
                             "a bit off.")


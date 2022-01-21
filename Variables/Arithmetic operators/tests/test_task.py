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
        expected_addition_result = 10.0

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

    def test_ordered_2_division_remainder(self):
        expected_division_remainder = 1

        try:
            actual_division_remainder = try_import().division_remainder
        except AttributeError:
            self.fail(msg="The variable division_remainder seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_division_remainder, actual_division_remainder, msg="The division remainder value "
                                                                                     "seems to be "
                                                                                     "a bit off.")

    def test_ordered_3_multiplication_result(self):
        expected_multiplication_result = 9.0

        try:
            actual_multiplication_result = try_import().multiplication_result
        except AttributeError:
            self.fail(msg="The variable multiplication_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_multiplication_result, actual_multiplication_result,
                         msg="The multiplication result value seems to be "
                             "a bit off.")

    def test_ordered_5_subtraction_result(self):
        expected_subtraction_result = 0

        try:
            actual_subtraction_result = try_import().subtraction_result
        except AttributeError:
            self.fail(msg="The variable subtraction_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_subtraction_result, actual_subtraction_result,
                         msg="The subtraction result value seems to be "
                             "a bit off.")

    def test_ordered_6_floor_result(self):
        expected_floor_result = 4.0

        try:
            actual_floor_result = try_import().floor_result
        except AttributeError:
            self.fail(msg="The variable floor_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_floor_result, actual_floor_result, msg="The floor result value seems to be "
                                                                         "a bit off.")

    def test_ordered_7_power_result(self):
        expected_power_result = 729.0

        try:
            actual_power_result = try_import().power_result
        except AttributeError:
            self.fail(msg="The variable power_result seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_power_result, actual_power_result, msg="The power result value seems to be "
                                                                         "a bit off.")
    # TODO: add operator priority test

import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import comparison_operators
    return comparison_operators


class TestCase(unittest.TestCase):
    task_name = 'comparison_operators'

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

    def test_greater(self):
        expected_is_greater = True

        try:
            actual_is_greater = try_import().is_greater
        except AttributeError:
            self.fail(msg="The variable is_greater seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_is_greater, actual_is_greater, msg="The is_greater variable has a wrong value. "
                                                                     "Make sure you use the correct operator.")

    def test_less(self):
        expected_is_less = True

        try:
            actual_is_less = try_import().is_less
        except AttributeError:
            self.fail(msg="The variable is_less seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_is_less, actual_is_less, msg="The is_less variable has a wrong value. "
                                                               "Make sure you use the correct operator.")

    def test_chained_arbitrary(self):
        expected_is_true = True

        try:
            actual_is_true = try_import().is_true
        except AttributeError:
            self.fail(msg="The variable is_true seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_is_true, actual_is_true, msg="The is_true variable has a wrong value. "
                                                               "Make sure you use correct operators.")

    def test_not_equal(self):
        expected_not_equal = True

        try:
            actual_not_equal = try_import().not_equal
        except AttributeError:
            self.fail(msg="The variable not_equal seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_not_equal, actual_not_equal, msg="The not_equal variable has a wrong value. "
                                                                   "Make sure you use the correct operator.")

    def test_equal(self):
        expected_is_equal = True

        try:
            actual_is_equal = try_import().is_equal
        except AttributeError:
            self.fail(msg="The variable is_equal seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_is_equal, actual_is_equal, msg="The is_equal variable has a wrong value. "
                                                                 "Make sure you use the correct operator.")

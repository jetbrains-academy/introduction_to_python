import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import boolean_operators
    return boolean_operators


class TestCase(unittest.TestCase):
    task_name = 'boolean_operators'

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

    def test_true(self):
        expected_value = True

        try:
            actual_value = try_import().is_true
        except AttributeError:
            self.fail(msg="The variable is_true seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The is_true variable has a wrong value. "
                                                                 "Make sure your comparison is to a correct value.")

    def test_false(self):
        expected_value = False

        try:
            actual_value = try_import().is_false
        except AttributeError:
            self.fail(msg="The variable is_false seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The is_false variable has a wrong value. "
                                                           "Make sure your comparison is to a correct value.")

    def test_equality_operator(self):
        expected_value = False

        try:
            actual_value = try_import().is_equal
        except AttributeError:
            self.fail(msg="The variable is_equal seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The is_equal variable has a wrong value. "
                                                           "Make sure your comparison is to a correct value.")

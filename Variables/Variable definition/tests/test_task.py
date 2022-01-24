import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import variable_definition
    return variable_definition


class TestCase(unittest.TestCase):
    task_name = 'variable_definition'

    def setUp(self):
        try:
            # Stores output from print() in actualOutput
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                # Loads submission on first test, reloads on subsequent tests
                if self.task_name in sys.modules:
                    importlib.reload(sys.modules[self.task_name])
                else:
                    importlib.import_module(self.task_name)
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for IDE-highlighted "
                      "errors and warnings.".format(str(e)))

    def test_assignment_operator(self):
        expected_first_greetings = "greetings = greetings"
        actual_output = self.actualOutput.getvalue()

        self.assertIn(expected_first_greetings, actual_output, msg="The line expressing greetings after the initial "
                                                                   "assignment was not found. Check that the variable is "
                                                                   "assigned properly and that the print statement "
                                                                   "is intact.")

    def test_assignment_operator2(self):
        expected_first_greetings = "greetings = greetings"
        actual_output = self.actualOutput.getvalue()

        self.assertIn(expected_first_greetings, actual_output, msg="The line expressing greetings after the initial "
                                                                   "assignment was not found. Check that the variable is "
                                                                   "assigned properly and that the print statement "
                                                                   "is intact.")

    def test_variable(self):
        unexpected_greetings = "greetings"

        try:
            actual_greetings = try_import().greetings
        except AttributeError:
            self.fail(msg="The variable greetings seems to be undefined. Do not remove it from the task code.")

        self.assertNotEqual(unexpected_greetings, actual_greetings, msg="The variable greetings doesn't seem to be "
                                                                        "reassigned. You should change it to something "
                                                                        "else.")

    def test_chained_assignment(self):
        expected_a = expected_b = 2

        try:
            actual_a = try_import().a
        except AttributeError:
            self.fail(msg="The variable a seems to be undefined. Do not remove it from the task code.")
        try:
            actual_b = try_import().b
        except AttributeError:
            self.fail(msg="The variable b seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_a, actual_a, msg="The variable a should be reassigned via chained assignment.")
        self.assertEqual(expected_b, actual_b, msg="The variable b should be assigned via chained assignment.")

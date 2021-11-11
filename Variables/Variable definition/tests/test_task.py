import contextlib
from io import StringIO
import sys
import unittest


@contextlib.contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


with captured_output() as (out, err):
    import variable_definition
    actual_output = out.getvalue()


class TestCase(unittest.TestCase):

    def test_assignment_operator(self):
        expected_first_greetings = "greetings = greetings"

        self.assertIn(expected_first_greetings, actual_output, msg="The line expressing greetings after the initial "
                                                                   "assignment was not found. Check if the variable is "
                                                                   "assigned properly and that the print statement "
                                                                   "is intact.")

    def test_variable_concept(self):
        unexpected_greetings = "greetings"

        try:
            actual_greetings = variable_definition.greetings
        except AttributeError:
            self.fail(msg="The variable greetings seems to be undefined. Do not remove it from the task code")

        self.assertNotEqual(unexpected_greetings, actual_greetings, msg="The variable greetings seems not to be "
                                                                        "reassigned. You should change it to something "
                                                                        "else.")

    def test_chained_assignment_operator(self):
        expected_a = expected_b = 2

        try:
            actual_a = variable_definition.a
        except AttributeError:
            self.fail(msg="The variable a seems to be undefined. Do not remove it from the task code")
        try:
            actual_b = variable_definition.b
        except AttributeError:
            self.fail(msg="The variable b seems to be undefined. Do not remove it from the task code")

        self.assertEqual(expected_a, actual_a, msg="The variable a should be reassigned via chained assignment")
        self.assertEqual(expected_b, actual_b, msg="The variable b should be assigned via chained assignment")

import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import functions
    return functions


class TestCase(unittest.TestCase):
    task_name = 'functions'

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

    def test_function_call(self):
        expected_output_my_function = "Hello, World!\n" \
                                      "Hello, World!\n" \
                                      "Hello, World!\n" \
                                      "Hello, World!\n" \
                                      "Hello, World!\n"

        actual_output_my_function = self.actualOutput.getvalue()

        self.assertIn(expected_output_my_function, actual_output_my_function, msg="The output is lacking the "
                                                                                  "\"Hello, World!\" expression "
                                                                                  "repeated 5 times. Make sure "
                                                                                  "my_function gets called inside the "
                                                                                  "loop with 5 iterations.")

    def test_function_definition(self):
        expected_function_output = "I want to be a function\n"

        try:
            actual_function = try_import().fun
        except AttributeError:
            self.fail(msg="There was a problem loading fun function. Make sure you declare it properly.")

        with patch('sys.stdout', new=StringIO()) as self.currentOutput:
            actual_function()
            actual_output = self.currentOutput.getvalue()

        self.assertEqual(expected_function_output, actual_output, msg="The result of the fun function is missing from "
                                                                      "the output. Make sure you declare it correctly."
                                                                      "Do not alter the body of the function.")

    # TODO test function purpose concept
    # TODO test def definition concept

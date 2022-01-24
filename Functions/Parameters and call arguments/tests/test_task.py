import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import param_args
    return param_args


class TestCase(unittest.TestCase):
    task_name = 'param_args'

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

    def test_arg_syntax_2(self):
        expected_square_result_2_is_4 = "4\n"

        try:
            actual_square = try_import().square
        except AttributeError:
            self.fail(msg="There was a problem loading the square function. Make sure you declare it properly.")

        with patch('sys.stdout', new=StringIO()) as self.currentOutput:
            actual_square(2)
            actual_output = self.currentOutput.getvalue()

        self.assertEqual(expected_square_result_2_is_4, actual_output, msg="The result of the square function is "
                                                                           "incorrect for argument 2. Check if you "
                                                                           "declare it properly.")

    def test_arg_syntax_3(self):
        expected_square_result_3_is_9 = "9\n"

        try:
            actual_square = try_import().square
        except AttributeError:
            self.fail(msg="There was a problem loading the square function. Make sure you declare it properly.")

        with patch('sys.stdout', new=StringIO()) as self.currentOutput:
            actual_square(3)
            actual_output = self.currentOutput.getvalue()

        self.assertEqual(expected_square_result_3_is_9, actual_output, msg="The result of the square function is "
                                                                           "incorrect for argument 3. Check if you "
                                                                           "declare it properly.")

    def test_arg_syntax_5(self):
        expected_square_result_5_is_25 = "25\n"

        try:
            actual_square = try_import().square
        except AttributeError:
            self.fail(msg="There was a problem loading the square function. Make sure you declare it properly.")

        with patch('sys.stdout', new=StringIO()) as self.currentOutput:
            actual_square(5)
            actual_output = self.currentOutput.getvalue()

        self.assertEqual(expected_square_result_5_is_25, actual_output, msg="The result of the square function is "
                                                                            "incorrect for argument 5. Check if you "
                                                                            "declare it properly.")

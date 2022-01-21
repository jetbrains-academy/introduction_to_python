import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import keyword_args
    return keyword_args


class TestCase(unittest.TestCase):
    task_name = 'keyword_args'

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

    def test_keyword_argument_syntax_1(self):
        expected_output_for_growl_and_soup = "-- This cat wouldn't growl if you gave it soup"
        actual_output = self.actualOutput.getvalue()

        self.assertIn(expected_output_for_growl_and_soup, actual_output, msg="The line about the cat performing an action"
                                                                             "in response to feeding is missing from "
                                                                             "the output. Make sure you insert "
                                                                             "parameters correctly.")

    def test_keyword_argument_syntax_2(self):
        expected_output_for_growl_and_soup = "-- Lovely fur, the Sphinx"
        actual_output = self.actualOutput.getvalue()

        self.assertIn(expected_output_for_growl_and_soup, actual_output, msg="The line about the cat's breed"
                                                                             " is missing from "
                                                                             "the output. Make sure you insert "
                                                                             "parameters correctly.")

    def test_keyword_argument_syntax_3(self):
        expected_output_for_growl_and_soup = "-- It's still hungry!"
        actual_output = self.actualOutput.getvalue()

        self.assertIn(expected_output_for_growl_and_soup, actual_output, msg="The line about the cat's state"
                                                                             " is missing from "
                                                                             "the output. Make sure you insert "
                                                                             "parameters correctly.")
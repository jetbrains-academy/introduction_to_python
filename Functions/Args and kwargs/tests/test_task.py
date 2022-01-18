import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import args_kwargs
    return args_kwargs


class TestCase(unittest.TestCase):
    task_name = 'args_kwargs'

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

    def test_formal_parameters_1(self):
        try:
            actual_phrases = try_import().phrases
        except AttributeError:
            self.fail(msg="There was a problem while loading the phrases variable. Make sure its declaration "
                          "remains intact.")

        self.assertIsInstance(actual_phrases, list, msg="The phrases should be stored in a list.")

    def test_formal_parameters_2(self):
        try:
            actual_keywords = try_import().keywords
        except AttributeError:
            self.fail(msg="There was a problem while loading the keywords variable. Make sure its declaration "
                          "remains intact.")

        self.assertIsInstance(actual_keywords, dict, msg="The keywords should be stored in a dictionary.")

    def test_formal_parameters_3(self):
        try:
            actual_phrases = try_import().phrases
        except AttributeError:
            self.fail(msg="There was a problem while loading the phrases variable. Make sure its declaration "
                          "remains intact.")

        expected_phrases_in_output = [phrase.upper() for phrase in actual_phrases]
        actual_output = self.actualOutput.getvalue()

        for expected_phrase in expected_phrases_in_output:
            self.assertIn(expected_phrase, actual_output, msg="Some of the phrases appear to be missing "
                                                              "from the output. Do not modify the body "
                                                              "of the cat for this test to pass.")

    def test_formal_parameters_4(self):
        try:
            actual_keywords = try_import().keywords
        except AttributeError:
            self.fail(msg="There was a problem while loading the phrases variable. Make sure its declaration "
                          "remains intact.")

        actual_output = self.actualOutput.getvalue()

        for actual_keyword in actual_keywords.values():
            self.assertIn(actual_keyword, actual_output, msg=f"Seems like {actual_keyword} is missing from the "
                                                             f"output. Make sure you insert the keywords "
                                                             f"correctly.")

import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import default_parameter
    return default_parameter


class TestCase(unittest.TestCase):
    task_name = 'default_parameter'

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

    def test_default_value_takes_1_argument(self):
        try:
            actual_hello = try_import().hello
        except AttributeError:
            self.fail(msg="There was a problem while loading the hello function. Make sure its declaration stays intact.")

        try:
            actual_hello("test_subject")
        except TypeError:
            self.fail(msg="Seems like the hello function is unable to take just one argument. "
                          "Make sure you provide the default value for the name argument.")

    def test_default_value_takes_2_arguments(self):
        try:
            actual_hello = try_import().hello
        except AttributeError:
            self.fail(msg="There was a problem while loading the hello function. Make sure its declaration stays intact.")

        try:
            actual_hello("test_subject", "test_name")
        except TypeError:
            self.fail(msg="Seems like the hello function is unable to take two arguments. ")

    def test_default_value_takes_name_argument(self):
        try:
            actual_hello = try_import().hello
        except AttributeError:
            self.fail(msg="There was a problem while loading the hello function. Make sure its declaration stays intact.")

        try:
            actual_hello("test_subject", name="test_name")
        except TypeError:
            self.fail(msg="Seems like the hello function is unable to take the name argument. "
                          "Make sure the second argument is called \"name\"")
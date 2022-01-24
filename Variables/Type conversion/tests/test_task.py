import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import type_cast
    return type_cast


class TestCase(unittest.TestCase):
    task_name = 'type_cast'

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

    def test_type_conversion(self):
        expected_type = int
        try:
            actual_converted_float_number = try_import().converted_float_number
        except AttributeError:
            self.fail(msg="The variable converted_float_number seems to be undefined. "
                          "Do not remove it from the task code.")

        # TODO comeback and switch it to another assert architecture if the render of the text is not fixed in task view
        self.assertIs(type(actual_converted_float_number), expected_type, msg="The variable doesn't seem to be an integer "
                                                                              "yet. Please convert it!")

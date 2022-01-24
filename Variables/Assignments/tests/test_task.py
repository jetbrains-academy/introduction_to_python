import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import assignments
    return assignments


class TestCase(unittest.TestCase):
    task_name = 'assignments'

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

    def test_augmented_assignment(self):
        expected_number = 12.0

        try:
            actual_number = try_import().number
        except AttributeError:
            self.fail(msg="The variable number seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertEqual(expected_number, actual_number, msg="The number variable has a wrong value. "
                                                             "Make sure you use augmented assignment!")

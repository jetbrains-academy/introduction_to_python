import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import undefined_variable
    return undefined_variable


class TestCase(unittest.TestCase):
    task_name = 'undefined_variable'

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

    def test_variable_name(self):
        with self.assertRaises(NameError, msg="Try printing a variable which was not defined."):
            try_import()

    # TODO add Reserved keywords check

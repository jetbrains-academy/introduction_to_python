import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):
    task_name = 'variable_type'

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

    def test_object_type(self):
        expected_output = "<class \'float\'>"
        actual_output = self.actualOutput.getvalue()

        # This does give a confusing start to the error message, but the default for assertIn is worse, as it
        # cannot render <class smth> correctly, and for me, the result is less intriguing this way.
        self.assertTrue(expected_output in actual_output, msg="The statement about the type of float_number is missing "
                                                              "from the output, or the variable's type has changed.")

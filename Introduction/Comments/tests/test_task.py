import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


def try_import():
    import comments
    return comments


class TestCase(unittest.TestCase):
    task_name = 'comments'

    def setUp(self):
        try:
            # Stores output from print() in actualOutput
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                # Loads submission on first test, reloads on subsequent tests
                if self.task_name in sys.modules:
                    importlib.reload(sys.modules[self.task_name])
                else:
                    importlib.import_module(self.task_name)
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for IDE-highlighted "
                      "errors and warnings.".format(str(e)))

    def test_assignment_operator(self):
        expected_absent_line = "This line should not be printed!"
        actual_output = self.actualOutput.getvalue()

        if expected_absent_line in actual_output:
            self.fail(msg="The line, which says it should not be printed, "
                          "should, in fact, not be printed.")

    def test_output_len(self):
        expected_out_len = 31
        actual_output = self.actualOutput.getvalue()
        print(actual_output)

        self.assertEqual(expected_out_len, len(actual_output), msg="The length of your output does not seem right. "
                                                                   "Please comment just one required line and do not "
                                                                   "remove or add anything else.")

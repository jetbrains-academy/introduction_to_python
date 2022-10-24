import unittest

from task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        test_list  = [i + 10 for i in my_inefficient_list]
        self.assertEqual(test_list, my_efficient_list,
                         msg="Each element of `my_efficient_list` should equal a corresponding element of `my_inefficient_list` plus 10.")

    def test_0_code_len(self):
        with open("task.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 11, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("task.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not (' for ' in code and " in " in code):
                self.fail(msg="Your solution should use list comprehension.")
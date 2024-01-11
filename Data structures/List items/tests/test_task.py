import unittest
from list_items import animals


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(['elephant', 'elephant', 'elephant'], animals,
                         msg='The resulting list does not match the expected one. It should contain three elephants.')

    def test_0_code_len(self):
        with open("list_items.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 11, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("list_items.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("animals[1:3]" in code):
                self.fail(msg="Your solution should use assignment to a slice.")
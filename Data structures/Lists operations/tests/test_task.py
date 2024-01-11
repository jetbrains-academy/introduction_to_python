import unittest
from list_operations import animals


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog', 'dinosaur'], animals,
                         msg='The resulting list does not match the expected one.')

    def test_dinosaur(self):
        try:
            self.assertTrue(animals[-1] == animals[6] == 'dinosaur', msg='The 7th (and the last) element'
                                                                         'has to be "dinosaur".')
        except IndexError:
            self.assertTrue(False, msg='The list appears to be too short.')

    def test_0_code_len(self):
        with open("list_operations.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 11, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("list_operations.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("[" in code and "]" in code):
                self.fail(msg="Your solution should use indexing.")
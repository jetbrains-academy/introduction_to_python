import unittest


class TestCase(unittest.TestCase):
    def test_indexing(self):
        try:
            from string_indexing import python, p_letter
            self.assertEqual(python[0], p_letter, msg="Make sure you get the first letter from the word Python.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

    def test_0_code_len(self):
        with open("string_indexing.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 5, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("string_indexing.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("[0]" in code):
                self.fail(msg="Your solution does not use string indexing.")



import unittest


class TestCase(unittest.TestCase):
    def test_add(self):
        try:
            from negative_indexing import long_string, exclamation
            self.assertEqual(long_string[-1], exclamation, msg="Make sure you get the last symbol of long_string.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

    def test_0_code_len(self):
        with open("negative_indexing.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 3, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("negative_indexing.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("[-1]" in code):
                self.fail(msg="Your solution does not use string indexing.")
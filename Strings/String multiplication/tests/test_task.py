import unittest


class TestCase(unittest.TestCase):
    def test_food(self):
        try:
            from string_multiplication import food
            self.assertEqual('couscous', food, msg="Wrong string result.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

    def test_0_code_len(self):
        with open("string_multiplication.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 3, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("string_multiplication.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            self.assertTrue("*" in code, msg="Your solution does not use string multiplication.")
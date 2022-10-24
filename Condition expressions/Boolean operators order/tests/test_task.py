import unittest

class TestCase(unittest.TestCase):
    def test_0_code_len(self):
        with open("boolean_order.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 8, msg="Please do not add or remove any lines from the code file.")

    def test_statement_0(self):
        name = "John"
        age = 17
        with open("boolean_order.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1][6:-2]
            self.assertTrue(eval(code), msg="Your expression does not evaluate to True")

    def test_statement_1(self):
        with open("boolean_order.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-1][6:-2]
            if not ("Jane" in code and "John" in code and "age" in code and "name" in code):
                self.fail(msg="Your expression does not check the values of the variables")

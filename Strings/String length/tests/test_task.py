import unittest

try:
    from len_function import first_half, index_to_slice, phrase

    class TestCase(unittest.TestCase):
        def test_string(self):
            self.assertEqual(phrase[:index_to_slice], first_half, msg="You seem to have gotten a wrong slice.")

        def test_index_type(self):
            self.assertTrue(type(index_to_slice) == int, msg="An index should be an integer.")

        def test_index(self):
            self.assertEqual(int(len(phrase) / 2), index_to_slice, msg="You got a wrong slicing index.")

        def test_0_code_len(self):
            with open("len_function.py", "r") as taskfile:
                lines = taskfile.readlines()
                self.assertTrue(len(lines) == 8, msg="Please do not add or remove any lines from the code file.")

        def test_statement_1(self):
            with open("len_function.py", "r") as taskfile:
                lines = taskfile.readlines()
                code = lines[-2]
                if not ("phrase[" in code):
                    self.fail(msg="Your solution should use slicing to get half of the string.")

        def test_statement_2(self):
            with open("len_function.py", "r") as taskfile:
                lines = taskfile.readlines()
                code = lines[-3]
                if not ("len(phrase)" in code):
                    self.fail(msg="Your solution should use the len() function to find the middle point.")


except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Do not rename any variables.")

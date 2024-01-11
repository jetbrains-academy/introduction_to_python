import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from join_method import fruits, separator, joined
output = f.getvalue().split('\n')[0]


class TestCase(unittest.TestCase):
    def test_out_str(self):
        self.assertEqual('I like apples and I like bananas and I like peaches and I like grapes', output,
                         msg='Your printed output does not match the expected one.')

    def test_joined(self):
        self.assertEqual(joined, separator.join(fruits), msg='Your `joined` string appears incorrect.')

    def test_0_code_len(self):
        with open("join_method.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 4, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("join_method.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-2]
            if not ("separator.join(" in code):
                self.fail(msg="Your solution should use the join() method.")


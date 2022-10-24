import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from dicts import phone_book
output = f.getvalue().split('\n')
result = output[3]


class TestCase(unittest.TestCase):
    def test_out_num(self):
        self.assertEqual(str(234), result,
                         msg="Your printed output does not match the expected one.")

    def test_dict(self):
        self.assertTrue("Jared" in phone_book.keys(), msg="You didn't add Jared.")
        self.assertTrue(phone_book['Jared'] == 570, msg="Jared's number should be 570.")
        self.assertTrue('Gerard' not in phone_book.keys(), msg="You didn't remove Gerard.")
        self.assertEqual({'Jane': 234, 'Jill': 345, 'Jared': 570}, phone_book,
                         msg="Your resulting dictionary seems to be off.")

    def test_0_code_len(self):
        with open("dicts.py", "r") as taskfile:
            lines = taskfile.readlines()
            self.assertTrue(len(lines) == 18, msg="Please do not add or remove any lines from the code file.")

    def test_statement_1(self):
        with open("dicts.py", "r") as taskfile:
            lines = taskfile.readlines()
            code = lines[-6]
            if not ('phone_book["Jared"]' in code or "phone_book['Jared']" in code):
                self.fail(msg="Your solution should use dictionary indexing to get Jared's phone.")
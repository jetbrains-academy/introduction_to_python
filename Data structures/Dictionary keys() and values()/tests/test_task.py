import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from dict_key_value import phone_book
output = f.getvalue().split('\n')
result = output[2]


class TestCase(unittest.TestCase):
    def test_out_str(self):
        self.assertEqual('dict_values([123, 234, 345, 456])', result,
                         msg="Your printed output does not match the expected one.")

    def test_dict(self):
        self.assertEqual({'John': 123, 'Jane': 234, 'Gerard': 345, 'Jill': 456}, phone_book,
                         msg='Do not change the dictionary contents.')



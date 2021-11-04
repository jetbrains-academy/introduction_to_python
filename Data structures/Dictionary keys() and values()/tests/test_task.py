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
        self.assertEqual(result, 'dict_values([123, 234, 345, 456])',
                         msg="Your printed output does not match the expected.")

    def test_dict(self):
        self.assertEqual(phone_book, {'John': 123, 'Jane': 234, 'Gerard': 345, 'Jill': 456},
                         msg='Do not change dictionary contents.')



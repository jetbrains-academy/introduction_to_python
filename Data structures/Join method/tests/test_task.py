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


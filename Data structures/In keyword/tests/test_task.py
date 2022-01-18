import contextlib
import io
import unittest

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from in_keyword import grocery_dict
output = f.getvalue().split('\n')
result_1 = output[1]
result_2 = output[2]


class TestCase(unittest.TestCase):
    def test_tomatoes(self):
        self.assertTrue(result_1 == 'True', msg="Are you sure that `grocery_dict` values do not contain number 6?")

    def test_basil(self):
        self.assertTrue(result_2 == 'False', msg="Are you sure that `grocery_dict` contains basil? It should not...")



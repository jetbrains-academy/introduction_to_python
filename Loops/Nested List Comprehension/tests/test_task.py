import unittest

from task import matrix, string


class TestCase(unittest.TestCase):
    def test_item_type(self):
        for row in matrix:
            for char in row:
                self.assertEqual(str, type(char), msg="Your matrix should contain only items of type `str`.")

    def test_matrix(self):
        test_matrix = [[i for i in string] for j in range(10)]
        self.assertEqual(test_matrix, matrix, msg="Your matrix does not match the expected")

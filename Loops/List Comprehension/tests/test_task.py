import unittest

from list_comprehension import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        test_list  = [i + 10 for i in my_inefficient_list]
        self.assertEqual(test_list, my_efficient_list,
                         msg="Each element of `my_efficient_list` should equal a corresponding element of `my_inefficient_list` plus 10.")

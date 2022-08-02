import unittest

from lists_to_dict import my_dict


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def test_dict(self):
        list_of_keys = ["key1", "key2", "key3"]
        list_of_values = [100, 200, 300]

        test_dict = {}
        for x in range(len(list_of_keys)):
            test_dict[list_of_keys[x]] = list_of_values[x]

        self.assertEqual(test_dict, my_dict, msg="my_dict seems off.")

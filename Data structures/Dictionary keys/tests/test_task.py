import unittest


class TestCase(unittest.TestCase):
    def test_dict(self):
        try:
            from dict_keys import ages_dict
            test_dict1 = {
                "Alice": 21,
                "Bob": 39,
                "George": 30,
                "Susanne": 27,
                "Bob2": 19,
                ("Ashley", "Alex", "Nancy"): 35
            }

            test_dict2 = {
                "Alice": 21,
                "Bob": 39,
                "George": 30,
                "Susanne": 27,
                "Bob2": 19,
                "Ashley": 35,
                "Alex": 35,
                "Nancy": 35
            }

            self.assertTrue(list(ages_dict.values()) == list(test_dict1.values()) or list(ages_dict.values()) == list(
                test_dict2.values()), msg="You dictionary probably has duplicate keys. Make them unique!")

        except TypeError as e:
            self.fail(
                msg=f"Error: {e}. Create individual key:value pairs for each person or replace the list with a tuple.")

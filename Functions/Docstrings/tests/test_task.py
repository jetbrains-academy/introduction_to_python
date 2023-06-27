import unittest

from docstrings import increment_list


class TestCase(unittest.TestCase):
    def test_doc(self):
        self.assertNotEqual(increment_list.__doc__, None, msg="Add the docstring to the function.")
        self.assertEqual(increment_list.__doc__, "This function adds 1 to each element of the list.", msg="The "
                                                                                                         "docstring "
                                                                                                         "seems to be "
                                                                                                         "different.")

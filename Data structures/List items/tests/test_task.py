import unittest
from list_items import animals


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(['elephant', 'elephant', 'elephant'], animals,
                         msg='The resulting list does not match the expected one. It should contain three elephants.')


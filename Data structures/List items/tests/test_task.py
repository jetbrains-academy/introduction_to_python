import unittest
from list_items import animals


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(animals, ['elephant', 'elephant', 'elephant'],
                         msg='The resulting list does not match the expected. It should contain three elephants.')


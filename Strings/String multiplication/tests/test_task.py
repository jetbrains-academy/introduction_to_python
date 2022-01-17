import unittest


class TestCase(unittest.TestCase):
    def test_food(self):
        try:
            from string_multiplication import food
            self.assertEqual('couscous', food, msg="Wrong string result.")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

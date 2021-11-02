import unittest

try:
    from string_multiplication import food

    class TestCase(unittest.TestCase):
        def test_add(self):
            self.assertEqual(food, 'couscous', msg="Wrong string result.")

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")




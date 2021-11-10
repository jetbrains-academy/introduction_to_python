import unittest


try:
    from str_and_repr import Cat

    class TestCase(unittest.TestCase):
        def test_str(self):
            cat = Cat('sphynx', 'Kitty')
            self.assertEqual(str(cat), "My sphynx cat's name is Kitty", msg='Check your __str__() method.')

        def test_repr(self):
            cat = Cat('sphynx', 'Kitty')
            self.assertEqual(repr(cat), "Cat, breed: sphynx, name: Kitty", msg='Check your __repr__() method.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')






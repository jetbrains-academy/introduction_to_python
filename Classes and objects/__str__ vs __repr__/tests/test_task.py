import unittest


try:
    from str_and_repr import Cat

    class TestCase(unittest.TestCase):
        def test_hasattr_repr(self):
            cat = Cat('sphynx', 'Kitty')
            actual_repr = repr(cat)
            self.assertFalse('Cat object at' in actual_repr, msg='Method __repr__() is not defined for class Cat. If you copied the solution, please check the indentation.')

        def test_hasattr_str(self):
            cat = Cat('sphynx', 'Kitty')
            actual_str = str(cat)
            self.assertFalse('Cat object at' in actual_str, msg='Method __str__() is not defined for class Cat. If you copied the solution, please check the indentation.')

        def test_str(self):
            cat = Cat('sphynx', 'Kitty')
            expected, actual = "My sphynx cat's name is Kitty", str(cat)
            self.assertEqual(expected, actual, msg='Check your __str__() method.')

        def test_repr(self):
            cat = Cat('sphynx', 'Kitty')
            expected, actual = "Cat, breed: sphynx, name: Kitty", repr(cat)
            self.assertEqual(expected, actual, msg='Check your __repr__() method.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')






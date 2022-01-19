import unittest


try:
    from class_instance_variables import Animals

    class TestCase(unittest.TestCase):
        def test_class(self):
            george = Animals('George', 'rabbit')
            expected, actual = 'pets', george.kind
            self.assertEqual(expected, actual, msg='Check your class variable.')

        def test_instance(self):
            george = Animals('George', 'rabbit')
            expected, actual = 'rabbit', george.species
            self.assertEqual(expected, actual, msg='Check your __init__() method and the species attribute.')
            expected, actual = 'George', george.name
            self.assertEqual(expected, actual, msg='Check your __init__() method and the name attribute.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')

except TypeError:
    class TestFailCase2(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='The __init__() method should accept three arguments: self, name, and species.')







import unittest


try:
    from class_instance_variables import Animals

    class TestCase(unittest.TestCase):
        def test_class(self):
            george = Animals('George', 'rabbit')
            self.assertEqual(george.kind, 'pets', msg='Check your class variable.')

        def test_instance(self):
            george = Animals('George', 'rabbit')
            self.assertEqual(george.species, 'rabbit', msg='Check your __init__() method and species attribute.')
            self.assertEqual(george.name, 'George', msg='Check your __init__() method and name attribute.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')

except TypeError:
    class TestFailCase2(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='__init__() method should accept three arguments: self, name and species.')







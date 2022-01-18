import unittest


try:
    from init_method import Car


    class TestCase(unittest.TestCase):
        def test_car(self):
            car = Car("blue", "BMW")
            expected, actual = 'blue', car.color
            self.assertEqual(expected, actual, msg='Check your __init__() method.')
            expected, actual = 'BMW', car.brand
            self.assertEqual(expected, actual, msg='Check your __init__() method.')

except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')

except TypeError:
    class TestFailCase2(unittest.TestCase):
        def test_dail(self):
            self.assertTrue(False, msg='The __init__() method needs to have 3 arguments.')





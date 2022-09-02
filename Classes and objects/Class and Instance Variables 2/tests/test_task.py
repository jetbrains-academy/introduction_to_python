import unittest

from task import City


class TestCase(unittest.TestCase):
    def test_city(self):
        malaga = City('Malaga', 569005, 'Spain')
        if hasattr(malaga, 'all_cities'):
            self.assertTrue(True)
        else:
            self.fail(msg='Add a mutable class variable (all_cities list) to store all added city names')

    def test_cities(self):
        malaga = City('Malaga', 569005, 'Spain')
        boston = City('Boston', 689326, 'USA')
        beijing = City('Beijing', 21540000, 'China')
        self.assertEqual(['Malaga', 'Boston', 'Beijing'], beijing.all_cities)

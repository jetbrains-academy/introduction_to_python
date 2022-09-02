import unittest

from task import Calculator


class TestCase(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        calc.add(5)
        self.assertEqual(5, calc.get_current(), msg="Something wrong with the add method.")

    def test_multiply(self):
        calc = Calculator()
        calc.add(5)
        calc.multiply(2)
        self.assertEqual(10, calc.get_current(), msg="Something wrong with the multiply method.")

    def test_exponentiate(self):
        calc = Calculator()
        calc.add(5)
        calc.multiply(2)
        calc.exponentiate(2)
        self.assertEqual(100, calc.get_current(), msg="Something wrong with the exponentiate method.")
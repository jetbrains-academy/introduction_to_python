"""
This module contains a calculator
"""


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def subtract(self, amount):
        self.current -= amount

    def multiply(self, amount):
        self.current *= amount

    def divide(self, amount):
        try:
            self.current /= amount
        except ZeroDivisionError:
            print('Can not divide by zero.')

    def get_current(self):
        return self.current

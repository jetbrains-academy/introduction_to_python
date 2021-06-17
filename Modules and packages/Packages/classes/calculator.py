"""
This module contains calculator classes
"""


class Add:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current


class Subtract:
    def __init__(self):
        self.current = 100

    def subtract(self, amount):
        self.current -= amount

    def get_current(self):
        return self.current


class Multiply:
    def __init__(self):
        self.current = 10

    def multiply(self, amount):
        self.current *= amount

    def get_current(self):
        return self.current

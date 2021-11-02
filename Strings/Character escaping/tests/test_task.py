import unittest
import io
import sys


def test_foo():
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    import character_escaping
    sys.stdout = sys.__stdout__  # Reset redirect.
    value = capturedOutput.getvalue()
    return value


class TestCase(unittest.TestCase):
    def test_string(self):
        result = test_foo()[:-1]
        string = 'The name of this ice-cream is "Sweet\'n\'Tasty"'
        answer = result == string
        # self.assertEqual(result, string, msg='Wrong result string.')
        self.assertTrue(answer, msg='Wrong result string.')

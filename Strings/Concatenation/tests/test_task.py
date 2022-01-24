import unittest


class TestCase(unittest.TestCase):
    def test_import_hello(self):
        try:
            from concatenation import hello_world
            self.assertEqual('Hello World', hello_world, msg="Wrong string result.")
            self.assertTrue(' ' in hello_world, msg='The string result should contain a space.')

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")



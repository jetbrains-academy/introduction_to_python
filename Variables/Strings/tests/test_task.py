import unittest

class TestCase(unittest.TestCase):
    def test_import_hello(self):
        try:
            from printing_your_name import name
            self.assertNotEquals('JetBrains', name, msg="You should type in your name!")

        except ImportError:
            self.assertTrue(False, msg="Do not rename any variables.")

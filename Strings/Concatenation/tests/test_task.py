import unittest

try:
    from concatenation import hello_world

    class TestCase(unittest.TestCase):
        def test_add(self):
            self.assertEqual(hello_world, 'Hello World', msg="Wrong string result.")

        def test_space(self):
            self.assertTrue(' ' in hello_world, msg='String result should contain a space.')

except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")




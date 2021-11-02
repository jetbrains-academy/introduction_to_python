import unittest

try:
    from string_multiplication import two_times_hello

    class TestCase(unittest.TestCase):
        def test_add(self):
            self.assertEqual(two_times_hello, 'hello-hello-hello-hello-hello-', msg="Wrong string result.")


except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")




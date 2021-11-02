import unittest

try:
    from len_function import first_half, index_to_slice, phrase

    class TestCase(unittest.TestCase):
        def test_string(self):
            self.assertEqual(first_half, phrase[:index_to_slice], msg="You seem to have gotten a wrong slice.")

        def test_index_type(self):
            self.assertTrue(type(index_to_slice) == int, msg="Index should be an integer.")

        def test_index(self):
            self.assertEqual(index_to_slice, int(len(phrase) / 2), msg="You got a wrong slicing index.")


except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertEqual(1, 2, msg="Do not rename any variables.")

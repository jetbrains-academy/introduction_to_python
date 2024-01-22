import unittest

try:
    from len_function import first_half, index_to_slice, phrase

    class TestCase(unittest.TestCase):
        def test_string(self):
            self.assertEqual(phrase[:index_to_slice], first_half, msg="You seem to have gotten a wrong slice.")

        def test_index_type(self):
            self.assertTrue(type(index_to_slice) == int, msg="An index should be an integer.")

        def test_index(self):
            self.assertEqual(int(len(phrase) / 2), index_to_slice, msg="You got a wrong slicing index.")


except ImportError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Do not rename any variables.")

except TypeError:
    class TestCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg="Don't forget to convert the result of division to int type")
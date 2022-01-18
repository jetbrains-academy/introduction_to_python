import unittest


try:
    from self_parameter import Calculator


    class TestCase(unittest.TestCase):
        def test_initial(self):
            value = Calculator()
            expected, actual = 0, value.current
            self.assertEqual(expected, actual, msg='Initial current value should be 0.')

        def test_add(self):
            value = Calculator()
            value.add(100)
            value.add(100)
            expected, actual = 200, value.current
            self.assertEqual(expected, actual, msg='Make sure you implemented the add method correctly.')

        def test_get_current(self):
            value = Calculator()
            value.add(100)
            expected, actual = value.current, value.get_current()
            self.assertEqual(expected, actual, msg='Method get_current() should return self.current.')


except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')




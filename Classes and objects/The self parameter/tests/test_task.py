import unittest


try:
    from self_parameter import Calculator


    class TestCase(unittest.TestCase):
        def test_initial(self):
            value = Calculator()
            self.assertEqual(value.get_current(), 0, msg='Initial current value should be 0.')

        def test_add(self):
            value = Calculator()
            value.add(100)
            value.add(100)
            self.assertEqual(value.current, 200, msg='Make sure you implemented the add method correctly.')

        def test_get_current(self):
            value = Calculator()
            value.add(100)
            self.assertEqual(value.current, value.get_current(), msg='Method get_current() should return self.current.')


except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class names.')




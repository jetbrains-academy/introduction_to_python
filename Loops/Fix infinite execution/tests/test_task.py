import unittest
from tests.decorated_test_function import test_that_can_take_too_long

timeoutlimit = 5


class TestCase(unittest.TestCase):
    def test_infinite(self):
        try:
            err = test_that_can_take_too_long()
            if err:
                self.fail(msg=err)
        except TimeoutError as e:
            self.fail(
                msg=f"TimeoutError after {timeoutlimit} seconds. Your method's execution does not seem to end in a "
                    "reasonable amount of time.")

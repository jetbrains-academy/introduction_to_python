import unittest
import contextlib
import io

import timeout_decorator

from task import should_not_be_infinite


class TestCaseWithTimeouts(unittest.TestCase):
    @timeout_decorator.timeout(2)
    def test_that_can_take_too_long(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            should_not_be_infinite()
        output = f.getvalue().split('\n')

        self.assertEqual(['Hello, World!', 'Hello, World!', 'Hello, World!', 'Hello, World!', 'Hello, World!', ''], output)



import unittest
import contextlib
import io
import datetime

f = io.StringIO()
with contextlib.redirect_stdout(f):
    import builtin_modules
output = f.getvalue().split('\n')
time_stamp = str(datetime.datetime.today())


class TestCase(unittest.TestCase):
    def test_datetime(self):
        self.assertEqual(time_stamp.split(':')[:2], output[1].split(':')[:2],
                         msg='Your code is not printing the correct current date and time.')




import unittest
import contextlib
import io

f = io.StringIO()

with contextlib.redirect_stdout(f):
    import packages
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_alex(self):
        expected, actual = 'See you later, Alex!', output[1]
        self.assertEqual(expected, actual,
                         msg='The second line of output should contain a goodbye to '
                             'Alex produced by the function `good_bye` that can be found in one of the modules.')

    def test_sam(self):
        expected, actual = 'Dear Sam, I am glad to finally meet you in person.', output[3]
        self.assertEqual(expected, actual,
                         msg='The fourth line of output should contain an official greeting for Sam.')

    def test_out_len(self):
        expected, actual = 5, len(output)
        self.assertEqual(expected, actual, msg='Please do not remove or add any print statements')





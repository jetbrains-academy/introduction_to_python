import contextlib
import io
import unittest


class TestCase(unittest.TestCase):
    def test_out(self):
        try:
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                from open_file import outfile
            output = f.getvalue().split('\n')

            expected, actual = 8, len(output)
            self.assertEqual(expected, actual, msg='Please do not remove or add any print statements.')
            self.assertTrue(outfile.closed, msg='outfile is not closed.')

        except ImportError:
            self.assertTrue(False, msg='Please do not rename any variables.')

        except NameError:
            self.assertTrue(False, msg='You should open input1.txt as `file`')


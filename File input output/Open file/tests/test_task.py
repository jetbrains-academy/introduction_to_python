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

            expected, actual = 6, len(output)
            self.assertEqual(expected, actual, msg='Please do not remove or add any print statements.')
            self.assertTrue(outfile.closed, msg='The outfile file is not closed.')
            with open('outfile.txt', 'r') as file:
                hello = file.readline()
                self.assertEqual('Hello World', hello, msg='Please do not remove write Hello World instruction')

        except ImportError:
            self.assertTrue(False, msg='Please do not rename any variables.')

        except NameError:
            self.assertTrue(False, msg='You should open input1.txt as a file.')

        except FileNotFoundError:
            self.assertTrue(False, msg='Output file name should be used from outfile_name variable.')

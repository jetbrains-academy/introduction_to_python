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

        # def test_out_len(self):
            self.assertEqual(8, len(output), msg='Please do not remove or add any print statements.')
            self.assertTrue(outfile.closed, msg='outfile is not closed.')

        except ImportError:
            # def test_fail(self):
                self.assertTrue(False, msg='Please do not rename any variables.')

        except NameError:
            # def test_fail1(self):
                self.assertTrue(False, msg='You should open input1.txt as `file`')


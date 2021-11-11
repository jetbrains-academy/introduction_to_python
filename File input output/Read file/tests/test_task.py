import contextlib
import io
import unittest


class TestCase(unittest.TestCase):
    def test_out(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            import read_file
        output = f.getvalue().split('\n')
        print(output)

        self.assertTrue(len(output) == 4 and output[2] == output[3] == '',
                        msg='Your output should only contain 2 lines.')
        self.assertEqual('I am a temporary file. Maybe someday, I\'ll become a real file.', output[0],
                         msg='The first line of output should be the line from input.txt.')
        self.assertEqual('My first line', output[1],
                         msg='The second line of output should be the first line from input1.txt.')

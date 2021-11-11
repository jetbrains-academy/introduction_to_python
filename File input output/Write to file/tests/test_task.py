import unittest
import write_to_file


class TestCase(unittest.TestCase):
    def test_out(self):
        with open('output.txt', 'r') as result:
            self.assertEqual('This is the output file.\n', result.readline(),
                             msg='First line in the output file should remain "This is the output file.".')
            self.assertEqual('lion and elephant and monkey\n', result.readline(),
                             msg='Second line in the output file should be "lion and elephant and monkey".')
            third_line = result.readline()
            self.assertTrue('15' == third_line or '15\n' == third_line,
                            msg='Third line in the output should be "15".')


import unittest
import write_to_file


class TestCase(unittest.TestCase):
    def test_first_line(self):
        with open('output.txt', 'r') as result:
            lines = result.readlines()
            expected, actual = 'This is the output file. Do not modify this line :)\n', lines[0]
            self.assertEqual(expected, actual,
                             msg='The first line in the output file should remain "This is the output file.Do not modify this line :)".')
    def test_last_line(self):
        with open('output.txt', 'r') as result:
            lines = result.readlines()
            actual = lines[-1]
            self.assertTrue('15' == actual or '15\n' == actual,
                             msg='The last line in the output should be "15".')

    def test_second_to_last_line(self):
        with open('output.txt', 'r') as result:
            lines = result.readlines()
            expected, actual = 'lion and elephant and monkey\n', lines[-2]
            self.assertEqual(expected, actual,
                             msg='The second to last line in the output file should be "lion and elephant and monkey".')


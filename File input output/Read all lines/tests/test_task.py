import contextlib
import io
import unittest

from read_all_lines import lines_list


class TestCase(unittest.TestCase):
    def test_out(self):
        with open("input.txt", "r") as f:
            expected_list = f.readlines()
        self.assertEqual(expected_list, lines_list, msg="lines_list does not match the expected list.")

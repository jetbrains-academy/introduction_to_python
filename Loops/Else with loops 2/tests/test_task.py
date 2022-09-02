import unittest
import contextlib
import io


from task import contains_even_number


class TestCase(unittest.TestCase):
    def test_even(self):
        f = io.StringIO()

        with contextlib.redirect_stdout(f):
            contains_even_number([1, 9, 37, 4])
        output = f.getvalue().split('\n')
        self.assertEqual(['List [1, 9, 37, 4] contains an even number.', ''], output, msg="Incorrect result for a "
                                                                                          "list with an even number.")

    def test_even_several_times(self):
        f = io.StringIO()

        with contextlib.redirect_stdout(f):
            contains_even_number([1, 9, 8, 8, 8])
        output = f.getvalue().split('\n')
        self.assertEqual(['List [1, 9, 8, 8, 8] contains an even number.', ''], output, msg="For a list with any "
                                                                                            "number of even values "
                                                                                            "the phrase 'List {lst} "
                                                                                            "contains an even number' "
                                                                                            "should only be printed "
                                                                                            "once. You might have "
                                                                                            "missed a break "
                                                                                            "statement.")

    def test_odd(self):
        f = io.StringIO()

        with contextlib.redirect_stdout(f):
            contains_even_number([1, 9, 37, 5])
        output = f.getvalue().split('\n')
        self.assertEqual(['List [1, 9, 37, 5] does not contain an even number.', ''], output, msg="Incorrect result "
                                                                                                  "for a list without"
                                                                                                  " an even number.")

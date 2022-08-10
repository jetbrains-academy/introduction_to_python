import unittest
import datetime
import contextlib
import io


class TestCase(unittest.TestCase):
    def test_indent(self):
        try:
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                import indentation
            output = f.getvalue().split('\n')

            if datetime.date.today().day < 15:
                exp_result = "It's the beginning of the month still!"
            else:
                exp_result = "It's not the beginning of the month anymore :("

            self.assertEqual(exp_result, output[0], "Only fix the indentation, please do not change anything else.")
            self.assertEqual('', output[1], "Only fix the indentation, please do not change anything else.")

        except IndentationError as e:
            self.fail(msg=f"Fix the code! IndentationError was raised: {e}")




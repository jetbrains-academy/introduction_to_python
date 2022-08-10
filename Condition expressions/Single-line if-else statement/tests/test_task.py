import unittest
import contextlib
import io


class TestCase(unittest.TestCase):
    def test_rand(self):
        f = io.StringIO()
        try:
            with contextlib.redirect_stdout(f):
                import task
            output = f.getvalue().split('\n')
            self.assertTrue(str(output[0][:2]).isnumeric() or output[0]=="Too small!")

        except SyntaxError as e:
            self.fail(msg=f"There's a syntax error in your code: {e}.")


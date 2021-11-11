import contextlib
import io
import unittest


class TestCase(unittest.TestCase):
    def test_string(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            import character_escaping
        output = f.getvalue()[:-1]
        string = 'The name of this ice-cream is "Sweet\'n\'Tasty"'
        self.assertEqual(string, output, msg='Wrong result string.')



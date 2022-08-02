import unittest
import contextlib
import io


f = io.StringIO()
with contextlib.redirect_stdout(f):
    import task

output = f.getvalue().split('\n')


class TestCase1(unittest.TestCase):
    def test_some_module(self):
        test_out = ['This is a message from some_module.', 'This is a message from task.', 'This is a message from the function in the imported module.', '']
        self.assertEqual(test_out, output, msg='Something is wrong, actual output does not match expected.')

    def test_some_main(self):
        self.assertFalse("This should not be printed" in output,
                         msg='You should move the last print statement in some_module into the `main` block.')

    def test_main_main(self):
        self.assertFalse("This should be printed ONLY when lists_to_dict.py is called directly." in output,
                         msg='You should move the last print statement in lists_to_dict.py into the `main` block.')

    def test_main_func(self):
        self.assertTrue('This is a message from the function in the imported module.' in output,
                        msg='Do not forget to call the function from the imported module.')
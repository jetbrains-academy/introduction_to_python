import wrapt_timeout_decorator
import contextlib
import io

from infinite import should_not_be_infinite

timeoutlimit = 5


@wrapt_timeout_decorator.timeout(timeoutlimit)
def test_that_can_take_too_long():
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        should_not_be_infinite()
    output = f.getvalue().split('\n')
    try:
        if ['Hello, World!', 'Hello, World!', 'Hello, World!', 'Hello, World!', 'Hello, World!', ''] == output:
            return
        else:
            raise AssertionError
    except AssertionError as e:
        return str(e)

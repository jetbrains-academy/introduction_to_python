import wrapt_timeout_decorator
from return_keyword import fib


@wrapt_timeout_decorator.timeout(5)
def decorated_test_keyword_return(val):
    result = fib(val)
    return result

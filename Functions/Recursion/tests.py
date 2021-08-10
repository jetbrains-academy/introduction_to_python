from test_helper import run_common_tests, failed, passed
from Functions.Recursion.recursion import factorial


def test_factorial5():
    if factorial(5) == 120:
        passed()
    else:
        failed("factorial of 5 should be 120!")


def test_factorial0():
    if factorial(1) == 1:
        passed()
    else:
        failed("factorial of 0 should be 1!")


def test_factorial10():
    if factorial(10) == 3628800:
        passed()
    else:
        failed("factorial of 10 should be 3628800!")


def test_factorial1():
    if factorial(1) == 1:
        passed()
    else:
        failed("factorial of 1 should be 1!")


if __name__ == '__main__':
    run_common_tests()
    test_factorial0()
    test_factorial5()
    test_factorial1()
    test_factorial10()

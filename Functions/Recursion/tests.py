from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "factorial(n - 1)" in window and "*" in window:
        passed()
    else:
        failed("Do not forget the recursive function call!")


if __name__ == '__main__':
    run_common_tests()
    test_window()

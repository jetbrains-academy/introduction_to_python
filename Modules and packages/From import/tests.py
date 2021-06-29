from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "from my_module import hello as hey" in window:
        passed()
    else:
        failed("Wrong import, check out hint 1")


def test_window_1():
    window = get_answer_placeholders()[1]
    if "hey('" in window or 'hey("' in window:
        passed()
    else:
        failed("Call the hey function and give it our name as a string!")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window_1()

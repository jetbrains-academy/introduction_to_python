from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "if i == 3:" in window:
        passed()
    else:
        failed("Add the correct condition!")


def test_window1():
    window = get_answer_placeholders()[1]
    if "break" in window:
        passed()
    else:
        failed("Break the loop!")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
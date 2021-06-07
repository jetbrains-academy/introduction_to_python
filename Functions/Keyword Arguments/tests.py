from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "soup" in window and "growl" in window and "Sphinx" in window:
        passed()
    else:
        failed("Input values seem to be off")


def test_window1():
    window = get_answer_placeholders()[0]
    if "action=" in window and "breed=" in window:
        passed()
    else:
        failed("You keyword argument syntax has room for improvement!")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()

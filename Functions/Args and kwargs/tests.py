from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "It is too fat." in window and "You are feeding your cat too much." in window:
        passed()
    else:
        failed("Something wrong in the phrases list")


def test_window1():
    window = get_answer_placeholders()[1]
    if ":" in window \
            and "state" in window \
            and "fat" in window \
            and "action" in window \
            and "eat" in window \
            and "breed" in window \
            and "Maine Coon" in window:
        passed()
    else:
        failed("You keyword arguments have room for improvement!")


def test_window2():
    window = get_answer_placeholders()[2]
    if "cat(" in window and "anything" in window and "*phrases" in window and "**keywords" in window:
        passed()
    else:
        failed("Your function call is wrong")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()

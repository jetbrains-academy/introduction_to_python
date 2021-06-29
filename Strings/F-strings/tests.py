from test_helper import run_common_tests, passed, failed, get_answer_placeholders, import_task_file, get_file_output


def test_window():
    windows = get_answer_placeholders()

    if windows[0][1:-1].isalpha():
        passed()

    else:
        failed("Your name should be spelled with English letters")


def test_window1():
    windows = get_answer_placeholders()

    if windows[1].isnumeric():
        passed()
    else:
        failed("Age should be a number")


def test_window2():
    windows = get_answer_placeholders()

    if windows[2] == '{name}':
        passed()
    else:
        failed("Use {} and the variable name in replacement fields")


def test_window3():
    windows = get_answer_placeholders()

    if windows[3] == '{age}':
        passed()
    else:
        failed("Use {} and the variable name in replacement fields")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_window3()

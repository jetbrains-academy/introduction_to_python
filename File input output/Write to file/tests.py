from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "'a'" in window or '"a"' in window:
        passed()
    else:
        failed("Use 'a' modifier to append lines to the end of file")


def test_window1():
    window = get_answer_placeholders()[1]
    if "f.write(" in window:
        passed()
    else:
        failed("Use 'write' method")


def test_window3():
    window = get_answer_placeholders()[1]
    if "\\n" in window:
        passed()
    else:
        failed("Write output starting from a new line")


def test_window4():
    window = get_answer_placeholders()[1]
    if "' and '.join(zoo)" in window or '" and ".join(zoo)' in window:
        passed()
    else:
        failed("Use the join method with the ' and ' separator.")


def test_window5():
    window = get_answer_placeholders()[2]
    if "\\n" in window:
        passed()
    else:
        failed("Write number starting from a new line")


def test_window6():
    window = get_answer_placeholders()[2]
    if "str(number)" in window:
        passed()
    else:
        failed("Convert number to string using str() method")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window3()
    test_window4()
    test_window5()
    test_window6()
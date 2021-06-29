from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    if "with open(" in window:
        passed()
    else:
        failed("Use with open syntax.")


def test_window1():
    window = get_answer_placeholders()[0]
    if "as file:" in window:
        passed()
    else:
        failed("The file should be named 'file'.")


def test_window2():
    window = get_answer_placeholders()[0]
    if "'r'" in window or '"r"' in window:
        passed()
    else:
        failed("Add the 'r' argument!")


def test_window3():
    window = get_answer_placeholders()[1]
    if 'outfile.close()' in window:
        passed()
    else:
        failed("Close the outfile properly, use the f.close() syntax.")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_window3()
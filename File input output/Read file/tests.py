from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    if "for" in window and "in f:" in window:
        passed()
    else:
        failed("Use a for loop to iterate over the file.")


def test_window2():
    window = get_answer_placeholders()[1]
    if "print(" in window:
        passed()
    else:
        failed("Print each line of the first file!")


def test_window3():
    default_error = "Use the 'readline' method"
    window = get_answer_placeholders()[2]
    output = list(filter(lambda x: x != "", get_file_output()))
    if len(output) == 2 and output[1] == "My first line":
        passed()
        return
    if "print" not in window:
        failed("Don't forget to print the line")
        return
    failed(default_error)


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()
    test_window3()
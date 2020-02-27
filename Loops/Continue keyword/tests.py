from test_helper import run_common_tests, passed, failed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    if "x" in window and "%" in window:
        passed()
    else:
        failed("Use % operator to check that x is even")


def test_output():
    numbers = ['0', '2', '4', '6', '8']
    output = get_file_output()
    if len(output) > 4:
        output = output[4:]
    if any(number in output for number in numbers):
        failed("Print only odd the numbers")
    else:
        passed()


if __name__ == '__main__':
    run_common_tests()
    test_output()
    test_window()

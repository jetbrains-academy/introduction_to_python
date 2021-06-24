from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_output():
    default_error = "Terminate the loop at number 3!"
    window1 = get_answer_placeholders()[0]
    window2 = get_answer_placeholders()[1]
    output = list(filter(lambda x: x != "", get_file_output()))
    if len(output) == 9 and output[8] == "Outside the for loop":
        passed()
        return
    if "i" not in window1 or "3" not in window1:
        failed("Set a condition comparing i with 3.")
        return
    if "break" not in window2:
        failed("Don't forget to break")
        return
    failed(default_error)


if __name__ == '__main__':
    run_common_tests()
    test_output()

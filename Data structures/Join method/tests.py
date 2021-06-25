from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_output():
    default_error = "Your output does not match the expected output!"
    window = get_answer_placeholders()[0]
    output = get_file_output()
    if "I like apples and I like bananas and I like peaches and I like grapes" in output:
        passed()
        return
    if "separator" not in window:
        failed("Use the predefined separator!")
        return
    if ".join(" not in window:
        failed("Use the join method!")
        return
    failed(default_error)


if __name__ == '__main__':
    run_common_tests()
    test_output()



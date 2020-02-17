from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_initial():
    window = get_answer_placeholders()[0]
    if window == "type your name":
        failed("You should modify the file")
    else:
        passed()

if __name__ == '__main__':
    run_common_tests("You should enter your name")
    test_initial()



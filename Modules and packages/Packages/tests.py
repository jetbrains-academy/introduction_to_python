from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "import functions.greeting.official as official" in window:
        passed()
    else:
        failed("Wrong import, check out the hints!")


if __name__ == '__main__':
    run_common_tests()
    test_window()

from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[1]
    if "MyClass()" in window:
        passed()
    else:
        failed('Instantiate x by "calling" the class object!')


if __name__ == '__main__':
    run_common_tests()
    test_window()

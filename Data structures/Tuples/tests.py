from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "len(" in window:
        passed()
    else:
        failed("Use len() function")

def test_window1():
    window = get_answer_placeholders()[1]
    if "fun_tuple" in window:
        passed()
    else:
        failed("Add a string 'fun_tuple' to your tuple")

def test_window2():
    window = get_answer_placeholders()[1]
    if "," in window:
        passed()
    else:
        failed("A trailing comma is required")


if __name__ == '__main__':
    run_common_tests("Use len() function")
    test_window()
    test_window1()
    test_window2()
from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "kind = 'pets'" in window or 'kind = "pets"' in window:
        passed()
    else:
        failed("Implement the class variable: kind = 'pets'")


def test_window_1():
    window = get_answer_placeholders()[1]
    if 'self.name = name' in window or 'self.species = species':
        passed()
    else:
        failed("Your instance variable implementation is incorrect")


def test_window_2():
    window = get_answer_placeholders()[2]
    if 'self.name = name' in window or 'self.species = species':
        passed()
    else:
        failed("Your instance variable implementation is incorrect")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window_1()
    test_window_2()
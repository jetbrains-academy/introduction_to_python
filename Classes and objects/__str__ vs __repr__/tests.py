from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "f'Cat, breed: {self.breed}, name: {self.name}'" in window or 'f"Cat, breed: {self.breed}, name: {self.name}"' in window:
        passed()
    else:
        failed("Your repr method seems off")


def test_window1_f():
    window = get_answer_placeholders()[1]
    if "f'" in window or 'f"' in window:
        passed()
    else:
        failed("Use f-string syntax!")


def test_window1():
    window = get_answer_placeholders()[1]
    if "My {self.breed}" in window and 'name is {self.name}' in window:
        passed()
    else:
        failed("Use {self.attribute} syntax inside the f-string and follow the order in which things are printed")


def test_window1_esc():
    window = get_answer_placeholders()[1]
    if "\'s" in window or '"' in window:
        passed()
    else:
        failed("Use character escaping for the apostrophe or use a different kind of enclosing quotes")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window1_f()
    test_window1_esc()
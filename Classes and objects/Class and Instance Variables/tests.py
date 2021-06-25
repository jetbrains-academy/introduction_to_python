from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_kind():
    window = get_answer_placeholders()[0]
    if "kind = 'pets'" in window or 'kind = "pets"' in window:
        passed()
    else:
        failed("Implement the class variable: kind = 'pets'")


def test_name():
    window = get_answer_placeholders()[1]
    if 'self.name = name' in window:
        passed()
    else:
        failed("Your 'name' instance variable implementation is incorrect")


def test_species():
    window = get_answer_placeholders()[2]
    if 'self.species = species' in window:
        passed()
    else:
        failed("Your 'species' instance variable implementation is incorrect")



if __name__ == '__main__':
    run_common_tests()
    test_kind()
    test_name()
    test_species()
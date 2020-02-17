from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders, get_file_output


def test_value():
    output = get_file_output()
    answer = ['It is a really long string', 'triple-quoted st']
    if 'to define multi-line strings' in output:
        failed("Too long string in the output")
    else:
        passed()

    if all(word in output for word in answer):
        passed()
    else:
        failed("Too short string in the output")

def test_value_python3():
    import sys
    if sys.version[0] != "3":
        passed()
        return
    try:
        import_task_file()
        passed()
    except TypeError:
        failed("Division operator returns float in Python 3. Use int() function to convert float to integer.")

if __name__ == '__main__':
    test_value_python3()
    run_common_tests()

    test_value()

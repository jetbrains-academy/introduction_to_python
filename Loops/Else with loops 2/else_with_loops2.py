def contains_even_number(lst):
    for i in lst:
        if i % 2 == 0:
            print(f"List {lst} contains an even number.")
            break
    else:
        print(f"List {lst} does not contain an even number.")


contains_even_number([1, 9, 8])
contains_even_number([1, 3, 5])
phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
index_to_slice = int(len(phrase) / 2)  # Get the index up to which you will slice.
first_half = phrase[:index_to_slice]  # Get the slice of the phrase.
print(first_half)

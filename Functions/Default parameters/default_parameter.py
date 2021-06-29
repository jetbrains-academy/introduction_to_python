def multiply_by(a, b=2, c=1):
    return a * b + c


print(multiply_by(3, 47, 0))  # Call function using custom values for all parameters
print(multiply_by(3, 47))  # Call function using default value for c parameter
print(multiply_by(3, c=47))  # Call function using default value for b parameter
print(multiply_by(3))  # Call function using default values for parameters b and c
print(multiply_by(a=7))  # Call function using default values for parameters b and c


def hello(subject, name="John"):
    print(f"Hello {subject}! My name is {name}")


hello("PyCharm", "Jane")  # Call "hello" function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm")  # Call "hello" function with "PyCharm as a subject parameter and default value for the name

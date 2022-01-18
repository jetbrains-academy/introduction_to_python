class MyClass:
    variable = 42

    def foo(self):  # We'll explain self parameter later
        print("Hello from function foo")


# `my_object` holds an object of the class "MyClass" that contains
# the `variable` and the `foo` function
my_object = MyClass()

my_object.foo()  # Calls the `foo` method defined in MyClass
print(my_object.variable)  # Prints the value of the `variable` attribute defined in MyClass

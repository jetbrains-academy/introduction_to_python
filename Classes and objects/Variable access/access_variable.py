class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self):     # We'll explain self parameter later
        return "Hello from function foo"


my_object = MyClass()
another_object = MyClass()

my_object.variable2 = 3     # Assign a new value to variable2 in my_object

print(my_object.variable2)
print(another_object.variable2)

print(my_object.variable1)
print(my_object.foo())

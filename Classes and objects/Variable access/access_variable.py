class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self):     # We'll explain self parameter later
        print("Hello from function foo")


my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3     # Assign a new value to variable2 in my_object

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()   # Call method foo() of object my_object

print(my_object.variable1)


a = 1
# We'll explain the expression str(a) later in the course.
# For now: it is used to convert the variable "a" into a string.
print("a = " + str(a))

# Assign "greetings" to the variable using the assignment operator
greetings = "greetings"
print("greetings = " + str(greetings))
# Reassign anything to the variable here
greetings = 5
print("greetings = " + str(greetings))


# This is called a "chained assignment". It assigns the value 2 to variables "a" and "b".
a = b = 2
print("a = " + str(a))
print("b = " + str(b))

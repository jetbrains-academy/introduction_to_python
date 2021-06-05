## Parameters and call arguments

Function parameters are defined inside the parentheses `()`, following the 
function name. A parameter acts as a variable name for an argument passed to the
function. 

The terms parameter and argument refer to the same thing: information 
that are passed into a function. However, a parameter is the variable listed 
inside the parentheses in the function definition, while an argument is the 
value that is sent to the function when it is called.

By default, a function must be called with the correct number of arguments. 
If your function expects 2 arguments, you have to call the function 
with 2 arguments:

```python
def my_function(name, surname):
    print(name + " " + surname)

my_function("Jon", "Snow")
```
Result:
```text
Jon Snow
```
However if you just supply it with one argument during the call:
```python
my_function("Sam")
```
A `TypeError` will be raised:
```text
TypeError                                 Traceback (most recent call last)
<ipython-input-29-40eb74e4b26a> in <module>
----> 1 my_function('Jon')

TypeError: my_function() missing 1 required positional argument: 'surname'
```

Define a function that prints the square of the passed parameter.  

<div class='hint'>Put parameter 'x' inside parentheses in function definition.</div>

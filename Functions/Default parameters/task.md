## Default parameters

It is also possible to define functions with a variable number of arguments. There are 
three forms, which can be combined. The most useful form is to specify a default value 
for one or more arguments. This creates a function that can be called with fewer 
arguments than it is defined with. For example, check out the first function in the code editor.
This function can be called in several ways:

- giving only the mandatory argument `a`: `multiply_by(3)`

- giving one of the optional arguments: `multiply_by(3, 47)`, or `multiply_by(3, c=47)`

- or even giving all arguments: `multiply_by(3, 47, 0)`

You can specify which argument you are providing in the function call, just like we did in the third case
with `c=47`. If you do not specify that, values will be assigned according to their order.
Do not put spaces around the `=` symbol in function calls and definitions.
 
Explore this topic further by reading <a href="https://docs.python.org/3/tutorial/controlflow.html#default-argument-values">this section</a>
of Python Documentation.

Add parameters to the `hello()` function and set a default value for the `name` parameter.  

<div class='hint'>Specify any default value for the <code>name</code> parameter.</div>

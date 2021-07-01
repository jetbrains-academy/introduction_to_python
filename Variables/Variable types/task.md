## Variable types

All data in a Python program is represented by objects or by relations between 
objects. Every object has an identity, a type, and a value. An object’s identity 
never changes once it has been created; you may think of it as the object’s 
address in memory.

An object’s `type` determines the operations that it supports (e.g., 
“does it have a length?”) and defines the possible values for objects of 
that type. The `type()` function returns an object’s type (which is an object itself). 
Like its identity, an object’s type is also unchangeable.

The value of some objects can change. Objects whose value 
can change are <i>mutable</i>; objects whose value is unchangeable once 
they are created are called <i>immutable</i>.

In Python, there are two main types of numbers: integers and floats. The most important 
difference between them is that a `float` is a number that has a decimal point, 
and an `int` is a number without a decimal point.  

For more information on this topic, refer to the "<a href="https://docs.python.org/3/reference/datamodel.html#objects-values-and-types">Objects, values and types</a>"
and "<a href="https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy">The standard type hierarchy</a>" sections in Python Documentation.


Print the type of the variable `float_number`.  

<div class="hint">
Check out how we determined the type of <code>number</code> on line 2 and do the same with <code>float_number</code>.</div>

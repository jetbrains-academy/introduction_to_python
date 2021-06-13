## Definition

Classes provide a means of bundling data and functionality together. Creating a new 
class creates a new type of object, allowing new instances of that type to be made.
Classes are essentially templates for creating your objects.
Each class instance (object) can have attributes attached to it for maintaining its state.
Functions of objects are called methods, and they can modify their state. Methods are 
defined by the object's class.

The simplest form of class definition looks like this:

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Class definitions, like function definitions (`def` statements) must be executed before 
they have any effect.

The statements inside a class definition will usually be function definitions, 
but other statements are allowed, and sometimes useful. The 
function definitions inside a class normally have a peculiar form of argument list, dictated 
by the calling conventions for methods — this is explained later.

Class objects support two kinds of operations: attribute references and instantiation.
Attribute references will be discussed in the next sections. Class instantiation uses 
function notation. Just pretend that the class object is a parameterless function that 
returns a new instance of the class. For example:

```python
class SomeClass:
    """A simple example class"""
    i = 12345

x = SomeClass()
```

`x = SomeClass()` creates a new instance of the class and assigns this object to the local 
variable `x`.



Assign a value to the `variable` inside `MyClass` and create an object `x` of the class `MyClass()`. 

<div class='hint'>Assign any value to <code>variable</code>.</div>

<div class='hint'>Look at the example in the text to figure out how to instantiate an object.</div>



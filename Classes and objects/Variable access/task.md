## Variable access

You can use attribute references to access variables inside an object.
Attribute references use the standard syntax for all attribute references 
in Python: `obj.name`. Valid attribute names are all the names that were in 
the class’s namespace when the class object was created. So, if the class 
definition looked like this:

```python
class MyClass:
    year = 2021

    def say_hello(self):
        return 'hello world'
```
then `MyClass.year` and `MyClass.say_hello` are valid attribute references returning an 
integer and a function object, respectively. Class attributes can be 
assigned to, so you can change the value of `MyClass.year` by assignment.

  
Check out our example and print the value of `variable1` from `my_object`.  

<div class='hint'>Access <code>variable1</code> using the <code>object.name</code> syntax.</div>

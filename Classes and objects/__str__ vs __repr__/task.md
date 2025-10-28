## \_\_str__ vs \_\_repr__ methods

Both `str()` and `repr()` methods in Python are used for string representation of an object,
but there are some differences.
For example:
```python
s = 'Hello World'
print (str(s))
print(repr(s))
```
```text
Hello World
'Hello World'
```
You can see that if we print a string using the `repr()` function, then it prints 
with a pair of quotes. `str()` is used for creating output for the user, while `repr()` 
is normally used for debugging and development. `repr()` needs to be unambiguous, 
and `str()` &mdash; to be readable.

Much like `__init__`, the methods `__repr__` and `__str__` are reserved in Python. 
The `print()` statement and the `str()` built-in function use the `__str__` method defined in the object's class
to display its string representation. The `repr()` built-in function uses the `__repr__` method 
defined in the object's class. 

Our own defined class should therefore have a `__repr__` if we need detailed information for debugging. 
Also, if we think it would be useful to have a string representation for users, we should create 
a `__str__` function. Check out another implementation of the class `ComplexNumber` in the code editor. Run the code
to see what each of the two `print` statements prints.

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/7139#str__-vs-__repr?utm_source=jba&utm_medium=jba_courses_links).

### Task
Implement `__str__` and `__repr__` methods for the class `Cat`. `__str__` method should return a string like this:
`"My siamese cat's name is Lucy"`;  `__repr__` method should return a string like this:
`"Cat, breed: siamese, name: Lucy"`. Use [f-strings](course://Strings/F-strings).



<div class="hint">Do not forget to use <code>self.attribute</code> syntax.</div>
<div class="hint"> Do not forget about character escaping to print the apostrophe.</div>
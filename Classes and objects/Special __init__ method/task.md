## Special &#95;&#95;init&#95;&#95; method

The instantiation operation (“calling” a class object) creates an empty object, 
but it is useful to create objects with instances customized to a specific 
initial state. Therefore, a class may define a special method named `__init__()`, 
like this:

```python
class MyClass:
    def __init__(self):
        self.data = []
```
`__init__` is one of the reserved methods in Python. If defined, the `__init__()` 
method is invoked automatically when an instance of the class is created,
and it initializes the object and its attributes. It always takes at least
one argument, `self`. So in our example, 
a new, initialized instance can be obtained by:

```python
x = MyClass()
```
The `__init__()` method may receive arguments for greater flexibility. 
In that case, arguments given to the class instantiation operator are passed 
on to `__init__()`. For example:
```python
class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part
        self.num = complex(self.r, self.i)

x = ComplexNumber(3.0, -4.5)  # Instantiating a complex number
x.num
```
```text
(3-4.5j)
```

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6669#def-__init?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, add parameters to the`__init__()` method of the `Car` class, so we can 
create it with a specified color and brand.  

<div class='hint'>Add three parameters &mdash; <code>self</code>, <code>color</code> and <code>brand</code>.</div>

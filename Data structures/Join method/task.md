## The join() method

`.join()` is, in fact, a string method, but we're discussing it now because it 
requires understanding of iterable objects, such as strings, lists, and tuples.
This [method](https://docs.python.org/3/library/stdtypes.html#str.join) provides a flexible way to create strings from iterable objects. 
It joins each element of an iterable (such as list, string, or tuple) by 
a string separator (a string on which the `join()` method is called) and 
returns a concatenated string. A `TypeError` will be raised if there are 
any non-string values in the iterable. 

The syntax of the `join()` method looks as follows:

```python
string.join(iterable)
```

Examples:

```python
string_ = 'abcde'  # a string iterable
tuple_ = ('aa', 'bb', 'cc')  # a tuple iterable
list_ = ['Python', 'programming language']  # a list iterable

print(' + '.join(string_))  # join with the ' + ' separator
print(' = '.join(tuple_))  # join with the ' = ' separator

sep = ' is a '
print(sep.join(list_))  # join with the ' is a ' separator
```
```text
a + b + c + d + e
aa = bb = cc
Python is a programming language
```

Assign a value to the  `joined` variable such that the `print` statement prints the following:
```text
I like apples and I like bananas and I like peaches and I like grapes
```

<div class="hint">Look closely at the examples and simply do the same!</div>
<div class="hint"><code>fruits</code> is your iterable here, and <code>separator</code> is the separator string.</div>
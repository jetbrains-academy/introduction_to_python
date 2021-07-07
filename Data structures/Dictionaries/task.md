## Dictionaries

A dictionary is similar to a list, except that you access its values by looking up a 
key instead of an index. A key can be any immutable type. Strings and numbers can 
always be keys; tuples can be used as keys if they contain only immutable objects. 
You can’t use lists as keys. 

Think of a dictionary as a set of <code>key: value</code> pairs, with the requirement 
that the keys are unique within one dictionary. Dictionaries are enclosed 
in curly braces, e.g., `dct = {'key1' : "value1", 'key2' : "value2"}`. A pair of 
braces creates an empty dictionary: `{}`.  

A dictionary can also be created with the `dict` constructor:
```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
print(a == b == c)
```
```text
True
```

You can access a value in a dictionary similarly to how you would access a value in a list,
but using a key instead of an index. More info about this data structure can be found 
<a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">here</a>.
  
Print Jane's phone number from the `phone_book`.  

<div class='hint'>Use dictionary indexing, e.g., <code>dct[key]</code></div>

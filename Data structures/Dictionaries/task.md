## Dictionaries

A dictionary is similar to a list, except that you access its values by looking up a 
key instead of an index. A key can be any immutable type. String and numbers can 
always be keys, tuples can be used as keys if they contain only strings, numbers, or 
tuples; if a tuple contains any mutable object either directly or indirectly, 
it cannot be used as a key. You can’t use lists as keys. 

You can think of a dictionary as a set of <code>key: value</code> pairs, with the requirement 
that the keys are unique within one dictionary. Dictionaries are enclosed 
in curly braces e.g. `dct = {'key1' : "value1", 'key2' : "value2"}`. A pair of 
braces creates an empty dictionary: `{}`.  

You can access a value in a dictionary similarly to how you would access a value in a list,
but using a key instead of an index. More info about this data type structure can be found 
<a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">here</a>.
  
Print Jane's phone number from the `phone_book`.  

<div class='hint'>Use dictionary indexing e.g. <code>dct[key]</code></div>

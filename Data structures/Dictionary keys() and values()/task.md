## Dictionary keys() and values()

There are many useful methods in dictionaries, such as `keys()`,  `values()`, and `items()`. 
The `keys()` method returns a view object that displays a list of all the keys in the dictionary in order of insertion. 
`values()` returns a new view of the dictionary’s values. When the `items()` method is called,
it returns a new view of the dictionary’s items as tuples in a list (`(key, value)` pairs).

The objects returned by `dict.keys()`, `dict.values()`, and `dict.items()` provide a 
dynamic view on the dictionary’s entries, which means 
that when the dictionary changes, the view reflects these changes.

You can explore the rest using &shortcut:CodeCompletion; after `dict_name` 
followed by a dot.

Read more about the operations that dictionaries support <a href="https://docs.python.org/3/library/stdtypes.html#typesmapping">here</a>.

Print all values from the `phone_book` .  

<div class='hint'>Use the method <code>values()</code>.</div>

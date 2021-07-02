## Tuples

Tuples represent another standard sequence data type.
They are almost identical to lists. The only significant difference between tuples and 
lists is that tuples are immutable: you cannot add, replace, or delete elements in 
a tuple. Tuples are constructed by comma-separated elements enclosed in parentheses, for 
example: 

```python
(a, b, c)
```
 
A special situation is the construction of tuples containing 0 or 1 items. 
Empty tuples are constructed by an empty pair of parentheses; 
a tuple with one item is constructed by following a value with a comma. For example:

```python
empty = ()
singleton = 'hello',    # <-- note the trailing comma
len(empty)
```
```text
0
```
```python
len(singleton)
```
```text
1
```
```python
singleton
```
```text
('hello',)
```

The statement `t = 12345, 54321, 'hello!'` is an example of tuple packing: the 
values `12345`, `54321`, and `hello!` are packed together in a tuple. 

Some other list methods are also 
applicable to tuples. You can read more about tuples <a href="https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences">here</a>.
  
Print the length of the tuple `alphabet`. Then create a tuple with a single element `'fun_tuple'`. 
You can run the code to see what it prints.  

<div class='hint'>Use the <code>len()</code> function.</div>

<div class='hint'>Don't forget the trailing comma.</div>

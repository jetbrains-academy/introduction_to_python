## String length

The `len()` method is used to count how many characters a string contains.

For example:
```python
s = "Hello World"
print(len(s))   # will print 11
```

Note that the result of the `/` division operation is of type float:
```python
a = 10/2
print(a)        # 5.0
print(type(a))  # <class 'float'>
```

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/5814?utm_source=jba&utm_medium=jba_courses_links).

### Task
Get the first half of the string stored in the variable `phrase`.  
Note: when getting the index, remember about type conversion.  

<div class='hint'>You need to obtain a slice of the string from its start  
to the middle point.</div>

<div class='hint'>Get the middle index by dividing the string length by 2. The 
division result needs to be an integer.</div>

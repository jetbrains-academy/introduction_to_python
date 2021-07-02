## Lists introduction

Python has a number of compound data types used to group data together. 
The most versatile is the list, which can be written as a series of comma-separated 
values (items) enclosed in square brackets, e.g., `lst = [item1, item2]`. 
Lists might contain items of different types, but usually all the items in a list 
are of the same type. Like strings, lists can be indexed and sliced (see [Lesson 3](course://Strings/String slicing)).
All slice operations return a new list containing the requested elements.

Lists also support operations like concatenation:

```python
squares = [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

You can explore lists in more detail by reading <a href="https://docs.python.org/3.9/tutorial/introduction.html#lists">this page</a>.

Use list slicing to print `[4, 9, 16]`.  

<div class='hint'>List slicing syntax looks just like that for strings: <code>lst[index1:index2]</code>.
Don't forget that the element with the index <code>index2</code> is not included!</div>

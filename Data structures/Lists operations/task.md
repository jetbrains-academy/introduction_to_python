## List operations

Unlike strings, lists are a mutable type, i.e., it is possible to
change their content using `lst[index] = new_item`.

```python
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
```
```text
64
```
```python
cubes[3] = 64  # replace the wrong value
cubes
```
```text
[1, 8, 27, 64, 125]
```

You can add new items at the end of the list by using the `append()` method or 
list concatenation. 

```python
squares = [1, 4, 9, 16, 25]
squares.append(6**2)
squares
```
```text
[1, 4, 9, 16, 25, 36]
```
  
Find out about many other useful list methods on <a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">this page</a>.

Replace `"dino"` with `"dinosaur"` in the `animals` list.  
<div class='hint'>Use list indexing operation and value assignment.</div>

## Nested Lists

A list can contain any kind of objects, even other lists (sublists). This 
data structure is known as a nested list.

You can use nested lists to arrange data into hierarchical structures.

A nested list can be created by writing a comma-separated sequence of sublists:

```python
nested_list = [[1, 2, 3], [4, 5], 6]
```

You can access items in a nested list using indices just like before:

```python
print(nested_list[1])
print(nested_list[2])
```
Output:
```text
[4, 5]
6
```
You can access items within sublists in a nested list using multiple indices.
To access number `1` from `nested_list`, use the index `0` twice. First, you access the element `[1,2,3]` and then, the first element of that sublist:
```python
print(nested_list[0][0])
```
Output:
```text
1
```
For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6938?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, use indexing to access and print elements `9` and `10` from of the nested list `my_list`. 

<div class="hint">If you're stuck, review the examples in the task description again.</div>
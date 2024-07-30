## List Comprehension

You can use a loop to build a list (or another data structure).
For example:

```python
my_list = []
for i in range(5):
    my_list.append(i)

print(my_list)
```
Output:
```text
[0, 1, 2, 3, 4]
```

This is nice, but quite bulky. List comprehension offers a more compact syntax when you want to create a new list based on the values of an existing list
or another iterable (tuple, string, array, range, etc.). It does the same task and simplifies the program. Typically, list comprehensions are written in a single line of code.

```python
my_list = [i for i in range(5)]
print(my_list)
```
Output:
```text
[0, 1, 2, 3, 4]
```
List comprehensions are also more efficient computationally than a `for` loop.

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6315?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, use list comprehension to build `my_efficient_list` from the elements of `my_inefficient_list`
by adding $10$ to each of them. For example, the first element of `my_inefficient_list` is $1 + 10 = 11$,
so the first element of `my_efficient_list` should be $11 + 10 = 21$, and so on.


<div class="hint">

In the example above, we used `i for i in range(5)`. You can modify `i` as you like 
right inside this expression. For example, to subtract `5` from every `i`, you can do 
`i - 5 for i in range(5)`.
</div>
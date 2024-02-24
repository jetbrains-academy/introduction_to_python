## Nested List Comprehension

Nested list comprehensions are simply list comprehensions nested within other 
list comprehension. This is quite similar to [nested loops](course://Loops/Nested for Loop).
Here is a program that builds a [nested list](course://Data structures/Nested Lists) using a nested loop:

```python
matrix = []

for i in range(3):

    # Append an empty sublist inside the list
    matrix.append([])

    for j in range(0, 10, 2):
        matrix[i].append(j)

print(matrix)
```
Output:
```text
[[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
```

The same can be done in just one line using nested list comprehension:

```python
matrix = [[j for j in range(0, 10, 2)] for i in range(3)]
print(matrix)
```
Output:
```text
[[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
```

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6938#nested-list-comprehension?utm_source=jba&utm_medium=jba_courses_links).

### Task

Create a $10×10$ `matrix` such that each row (sublist) contains **characters** 0–9 from
`string`. Use list comprehension to complete the task in one line of code. 

<div class="hint">

Follow the example in the task description. You simply need to use `string` as an iterable instead
of one of the ranges.

</div>




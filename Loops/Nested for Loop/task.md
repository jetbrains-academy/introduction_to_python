## Nested Loops

A nested loop is a loop inside another loop.
The inner loop is executed once for each iteration of the outer loop.

```python
adjectives = ["black", "stylish", "expensive"]
clothes = ["jacket", "shirt", "boots"]

for x in adjectives:
  for y in clothes:
    print(x, y)
```
Output:
```text
black jacket
black shirt
black boots
stylish jacket
stylish shirt
stylish boots
expensive jacket
expensive shirt
expensive boots
```
<details>

Note that any type of loop can be nested inside another loop. 
For example, a [`while` loop](course://Loops/While loop) (see further) can be nested inside a `for` loop, or vice versa.
</details>

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6065#nested-loop?utm_source=jba&utm_medium=jba_courses_links).

### Task
You are given a tic-tac-toe board of 3x3, your task is to print every position. Coordinates along each side
are stored in the list `coordinates`. The output should be:
```text
1 x 1
1 x 2
1 x 3
2 x 1
...
```
and so on for every combination of coordinates.

<div class="hint">

In the nested `for` loop, iterate over the same list once again but using another variable name
this time (`coordinate2`).
</div>
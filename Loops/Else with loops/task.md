## Else with loops

We saw that the `break` statement breaks out of the innermost enclosing `for` or `while` loop.

Python also allows loop statements to have an `else` clause. It is executed when the loop terminates
through exhaustion of the iterable (with `for`) or when the condition becomes `False`
(with `while`), but not when the loop is terminated by a `break` statement. Check
out this example of a loop which searches for prime numbers:

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
```text
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
In this code, the `else` clause belongs to the `for` loop, not the
`if` statement.

Remember, an `else` after an `if` statement is skipped and NOT executed if the expression following 
`if` is `True`, while in the case of loops, an `else` clause is executed after the loop itself
is completed (unless there was a `break` in there somewhere).

In the code editor, add two lines of code to the second loop to make sure the loop prints
numbers 1 and 2 and never prints the phrase `"for loop is done"`.

<div class="hint">It should terminate at number 3.</div>
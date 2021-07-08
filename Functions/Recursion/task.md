## Recursion

The word <b>recursion</b> comes from the Latin word <i>recurrere</i>, meaning to return, revert, or recur.
In programming, recursion refers to a coding technique in which a function calls itself.

In most cases, recursion isn't necessary, but in some situations, self-referential
definition is warranted. Walking through tree-like data structures would be a good example.
Such structures are nested, and they readily fit a recursive definition. A non-recursive
algorithm for the same task would be quite cumbersome.  

Here's a simple example of a recursive function. It takes a number as an argument 
and prints the numbers from the specified argument down to zero. In the recursive call, 
the argument is one less than the current value of `n`, so each recursion moves closer 
to the base case (which is zero).

```python
def countdown(n):
    print(n, end=' ')
    if n == 0:
        return             # Terminates recursion
    else:
        countdown(n - 1)   # Recursive call


countdown(4)
```
```text
10 9 8 7 6 5 4 3 2 1 0 
```

<div class="hint">This function doesn’t check its argument for validity: if <code>n</code> 
is either a non-integer or negative, you’ll get a <code>RecursionError</code> exception because the base case is never reached:

```python
countdown(-10)
```
```text
RecursionError: maximum recursion depth exceeded while calling a Python object
```
You can find out what Python’s recursion limit is with a function from the sys module 
called `getrecursionlimit()`, and you can change it with `setrecursionlimit()`:

```python
from sys import setrecursionlimit
setrecursionlimit(3000)
getrecursionlimit()
```
```text
3000
```
</div>

Keep in mind that recursion isn’t useful in every situation. For some problems, a recursive solution, although 
possible, will be awkward rather than elegant. Recursive implementations often consume more 
memory than non-recursive ones and in some cases may result in slower execution.

In the code editor, implement a recursive function that calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of a positive integer.
For 1 and 0 it returns 1, for every other number it calculates the product of this number (`n`) and
the factorial of the previous number (`n-1`).

<div class="hint">Do not forget about the recursive function call.</div>



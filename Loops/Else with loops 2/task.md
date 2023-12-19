## Else with loops 2

This type of `else` is useful only if there is an `if` condition present inside the loop, which somehow depends on the loop variable.
Let's look once again at the example from the previous task:

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

The `else` statement will only be executed if `n` is a prime number, i.e. the `if` statement has not been executed for any iteration of the inner
`for` loop. 

### Task
Inside the [function](course://Loops/Else with loops 2) `contains_even_number()`, write a `for` loop that would iterate over a list `lst` and, if an even element is found,
print `f"List {lst} contains an even number."` and exit the loop, if no such element is found, print `f"List {lst} does not contain an even number."`. 

<div class="hint">

You can use `if i % 2 == 0:` to test if a given number is even.
</div>

<div class="hint">

Use the `break` statement to exit the loop if an even number is found.
</div>

<div class="hint">

Use an `else` clause to print `f"List {lst} does not contain an even number."`.
</div>
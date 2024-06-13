## Arithmetic operators

Just as in any other programming language, the addition ( `+` ), subtraction ( `-` ), 
multiplication ( `*` ), and division ( `/` ) operators can be used with numbers. In 
addition, Python has the power ( `**` ),  modulo ( `%` ), and floor division ( `//` ) operators.

- The `*` (multiplication) operator yields the product of its arguments. The arguments must 
either both be numbers, or one argument must be an integer and the other – a sequence.
  
- The `/` (division) and `//` (floor division) operators yield the quotient of their arguments. 
  Division of integers yields a float, while floor division of integers results in an integer.
  
- The `%` (modulo) operator yields the remainder of the division of the first argument by the second.

- The `+` (addition) operator yields the sum of its arguments. The arguments must either both 
  be numbers or both be sequences of the same type.
  
- The `-` (subtraction) operator yields the difference of its arguments.

For example
```python
a = 16
b = 3
result = a // b  # result will be 5
result = a % b   # result will be 1
result = a ** 2  # result will be 256 (16 in power of 2)
```

The binary arithmetic operations have the conventional priority levels. Note that 
some of these operations also apply to certain non-numeric types.

You can read more on this topic <a href="https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations">here</a>.

For more structured and detailed information, you can also refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/5865?utm_source=jba&utm_medium=jba_courses_links).

### Task
 - Divide the value stored in `init_number` by `2`.
 - Calculate a remainder of such a division.
 - Multiply the `division_result` by `2`.
 - Add the `division_remainder` to the `multiplication_result`.
 - Subtract the `multiplication_result` from the `init_number`.
 - Perform a floor division of `init_number` by 2.
 - Raise the `multiplication_result` to the power of 3

<div class='hint'>First, use the <code>/</code> operator.</div>
<div class='hint'>Then use the <code>%</code> operator.</div>

<div class='hint'>Then use the <code>*</code> operator.</div>

<div class='hint'>Then use the <code>+</code> operator.</div>

<div class='hint'>Then use the <code>-</code> operator.</div>

<div class='hint'>Then use the <code>//</code> operator.</div>

<div class='hint'>Then use the <code>**</code> operator.</div>

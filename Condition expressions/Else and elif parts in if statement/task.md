## Else and elif statements

The `elif` and `else` statements complement the `if` statement. 
There can be zero or more `elif` parts, and the `else` part is optional. The keyword 
`elif` is short for ‘else if’, and is useful to avoid excessive indentation.

<div class="hint">An <code>if … elif … elif …</code> sequence is a substitute for the <code>switch</code> or 
<code>case</code> statements found in other languages, such as Java.</div>

In conditional execution, only one of the suites is selected by evaluating the expressions one by one until one is found 
to be `True`. Then that suite is executed and no other part of the `if` statement is evaluated. 
If all expressions are false, the suite of the `else` clause, if present, is executed.


```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
```text
a is greater than b
```
  
Print `True` if `name` is equal to `"John"` and `False` otherwise.  

<div class='hint'>Use the <code>if</code> keyword and the <code>==</code> operator.</div>
<div class='hint'>Use the <code>else</code> keyword.</div>

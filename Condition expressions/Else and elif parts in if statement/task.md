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

<details>

A simple if-else statement can also be fit in one line of code, just like we have shown in the previous task. For example,
```python
if a > b:
    a += 1
else: 
    a -= 1
```
can be written as
```python
a += 1 if a > b else a -= 1
```
</details>
  
For more structured and detailed information, you can refer to [this](https://hyperskill.org/learn/step/5932?utm_source=jba&utm_medium=jba_courses_links) and [this](https://hyperskill.org/learn/step/5926?utm_source=jba&utm_medium=jba_courses_links) Hyperskill knowledge base pages.

### Task
Print `True` if `name` is equal to `"John"` and `False` otherwise.  

<div class='hint'>Use the <code>if</code> keyword and the <code>==</code> operator.</div>
<div class='hint'>Use the <code>else</code> keyword.</div>

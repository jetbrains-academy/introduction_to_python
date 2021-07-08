## If statement

Compound statements in Python contain (groups of) other statements; they affect or control 
the execution of those other statements in some way.

Perhaps the most well-known statement type is the `if` statement. The `if` keyword is 
used to form a conditional statement that executes some 
specified code after checking if its expression is `True`. Python uses indentation 
to define code blocks: 

```python
if value > 1000: 
    print("It's a large number!")  # Indented block
    a += 1                         # Indented block
    
print("Outside the block!")        
```

A code block starts with indentation and ends with the first unindented line. The amount of indentation must 
be consistent throughout the block. Generally, four whitespaces or single tabs are used for indentation.
Incorrect indentation will result in `IndentationError`.

If you have only one statement to execute, you can put it on the same line as the `if` statement.

```python
if a > b: print("a is greater than b")
```

Print `"empty"` if the `tasks` list is empty.  

<div class='hint'>Use the <code>len()</code> function to check if <code>tasks</code> is empty.</div>

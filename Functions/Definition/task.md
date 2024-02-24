## Definition

Functions are a convenient way to divide your code into useful blocks, make it more
readable, and reuse it.
The keyword `def` introduces a function definition.
It must be followed by the function name and the parenthesized list of **formal parameters** (which can be empty).
The statements that form the body of the function start at the next line and must be indented.

<details>
Formal parameters are enclosed in parentheses; they are the variables defined by the function, which receive values when the function is called. The list consists of variable names of all the necessary values for the method. Each formal parameter is separated by a comma. When the method is not accepting any input values, it should have an empty set of parentheses after the method name, e.g., <code>addition()</code>.
</details>

Functions only run when they are called. To call a function, use its name followed by parentheses:

```python
def my_function():  # function definition
  print("Hello from a function")

my_function()  # function call
```

Read more about defining functions in <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions">this section</a> of Python Documentation.

For more structured and detailed information, you can also refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/5900?utm_source=jba&utm_medium=jba_courses_links).

### Task
 - Call the function `my_function` inside the loop to repeat its invocation 5 times
 - Define a function that can replace the duplicated `print` statements in the file.  

<div class='hint'>Use the <code>()</code> to call the <code>my_function</code> function.</div>
<div class='hint'>Use the <code>def</code> keyword to define the <code>fun</code> function.</div>

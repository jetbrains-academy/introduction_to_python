## Return value

Functions may return a value to the caller, using the keyword `return` . You can use the 
returned value to assign it to a variable or just print it out. In fact, even functions 
without a `return` statement do return a value. This value is 
called `None` (it’s a built-in name). Writing the value `None` is normally suppressed by 
the interpreter, but if you really want to see it, you can use `print(some_func())`.

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/5900#execution-and-return?utm_source=jba&utm_medium=jba_courses_links).

><i>The first statement of the function body can optionally be a string literal; this string 
literal is the function’s documentation string, or docstring (more about docstrings can 
be found in the section <a href="https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings">Documentation Strings</a>
in Python Documentation). It’s good practice to include docstrings in the code that you write.</i>
  
In the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number), the first two numbers are `1` and `1` (sometimes, though, they are `0` and `1` or `1` and `2`), and each subsequent 
number is the sum of the previous two. 

### Task
Write a function that returns a list of numbers 
of the Fibonacci sequence up to `n` .  

<div class='hint'>Initialize <code>b</code> with 1.</div>
<div class='hint'>Update <code>b</code> with <code>a + b</code>.</div>
<div class='hint'>Update <code>a</code> with <code>tmp_var</code>.</div>



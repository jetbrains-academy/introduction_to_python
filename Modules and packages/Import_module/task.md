## Import module

As your program gets longer, you may want to split it into several files for 
easier maintenance. You may also want to use a handy function that you’ve written 
in several programs without copying its definition into each of them.

Modules in Python are simply Python files with the `.py` extension containing 
Python definitions and statements.
Modules are imported from other modules using the `import` keyword 
and the file name without the extension `.py`. 

Let's say you wrote a script called `my_funcs.py` with a bunch of functions (`func1`, `func2`, 
etc.). Now, if you want to use those in another script that is placed in the same directory, 
you can do `import my_funcs`. This does not import the names of the functions defined in `my_funcs` 
directly, but using the module name, you can now access the functions, for example:
```python
my_funcs.func1()
```
  
For more structured and detailed information, you can also refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6019#module-loading?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, you have already imported the module `my_funcs`. 
Call the function `hello_world` from this module with the argument `"John"`.

<div class='hint'>Access the function from the module using syntax such as <code>module.function()</code>.</div>
<div class="hint">Don't forget to provide the function with an argument.</div>


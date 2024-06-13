## Executing modules as scripts

A Python module is a file containing executable statements as well as function or class definitions. 
These statements are executed the first time the module name is encountered in an `import` statement.
The file name is the module name with the suffix .py appended. Within a module, the 
module’s name (as a string) is available as the value of the global variable `__name__`.


When you run a module **directly** (that is, not by importing it into another one),
the code in the module will be executed, just as if you imported it, but with 
`__name__` set to `"__main__"`. 

You can use `__name__` and `__main__` like this:

```python
if __name__ == "__main__":
   # Do something here
```

The statements inside this block will be executed only if the module is run directly and not through import
into another module. For example, let's consider two files:

main_program:
```python
import some_module

print(f"main_program __name__ is: {__name__}")

if __name__ == "__main__":
   print("main_program executed directly")
else:
   print("main_program executed when imported")
```

some_module:
```python
print(f"some_module __name__ is: {__name__}")

if __name__ == "__main__":
   print("some_module executed directly")
else:
   print("some_module executed when imported")
```

Output after running `main_program`:
```text
some_module __name__ is: some_module
some_module executed when imported
main_program __name__ is: __main__
main_program executed directly
```

Output after running `some_module`:
```text
some_module __name__ is: __main__
some_module executed directly
```

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6057?utm_source=jba&utm_medium=jba_courses_links).

### Task
<i>The files in this task are named the same as in the examples above, but their code is a bit different.</i>

Modify `task.py` and `some_module.py` so that when you run `task.py`, your output is as follows:

```text
This is a message from some_module.
This is a message from __main__.
This is a message from the function in the imported module.
This should be printed ONLY when task.py is called directly.
```
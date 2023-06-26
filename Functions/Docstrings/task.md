## Docstrings

One-line docstrings are for really obvious cases. Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description.
A docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.


Docstrings should also generally be written for module, class and method definitions (you will learn about these things later on in the course). Read more about docstring conventions in the [Python PEP Guide](https://peps.python.org/pep-0257/).

### Task 
Add the following docstring to the function defined in the code editor:
```text
"""This function adds 1 to each element of the list."""
```
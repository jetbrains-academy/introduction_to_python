## Packages

Packages are a way of structuring Python’s module [namespace](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) by using “dotted module 
names”. For example, the module name `A.B` designates a submodule named `B` in a package 
named `A`. Just like the use of modules saves the authors of different modules from 
having to worry about each other’s global variable names, the use of dotted module 
names saves the authors of multi-module packages like [NumPy](https://numpy.org/) 
or [Pillow](https://pypi.org/project/Pillow/) from having to worry about each other’s 
module names.

<div class="hint">The <code>__init__.py</code> files are required to make Python treat directories 
containing the file as packages. This prevents directories with a common name, such 
as <code>string</code>, from unintentionally hiding valid modules that occur later on the module search 
path. In the simplest case, <code>__init__.py</code> can just be an empty file.</div>

Check out the packages `functions` and `classes` we've created. Users of the packages 
can import individual modules from the package, for example:

```python
import functions.greeting.hello
```

This loads the submodule `functions.greeting.hello`. It must be referenced with its full name:

```python
functions.greeting.hello.hello('Susan')
```
An alternative way of importing the submodule is:

```python
from functions.greeting import hello
```

This also loads the submodule `hello`, and makes it available without its package prefix, 
so it can be used as follows:

```python
hello.hello('Susan')
```

You can learn more about packages by reading <a href="https://docs.python.org/3/tutorial/modules.html#packages">this page</a> of Python Documentation.

For more structured and detailed information, you can also refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6384?utm_source=jba&utm_medium=jba_courses_links).

### Task
Look at the file structure in the `classes` and `functions` directories and their subdirectories.

In the code editor, import the `official` module properly to make the last `print` 
statement work.

In the second print statement, add a function call (find the right function) so that it prints a goodbye to `'Alex'`.

<div class="hint">Access the module using syntax such as <code>package.subpackage.module</code>.</div>
<div class="hint">Use syntax such as <code>import module as something</code>.</div>
<div class="hint">Check out imports: there's one that might have the right function for the second task.
Be careful when using it: the module is already imported with a specific name.</div>

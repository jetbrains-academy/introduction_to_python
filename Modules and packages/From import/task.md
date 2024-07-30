## from import

One form of the import statement imports names `from` a module directly. This way, you 
can use the imported name without the `module_name` prefix.  For example:

```python
from calculator import Add

calc = Add()    # name `Add` used directly without prefix `calculator`
```

This does not introduce the name of the module from which the imports are taken in the 
local symbol table (so in our example, `calculator` is not defined).

There is even an option to import all names that a module defines:
```python
from calculator import *
calc = Multiply()
```
This imports all names except those beginning with an underscore `_`. 
In most cases, Python programmers do not use this, since it introduces 
an unknown set of names into the interpreter, possibly hiding some things 
you have already defined.

If the module name is followed by `as`, then the name following `as` is bound 
directly to the imported module:

```python
import my_module as mm
mm.hello_world()
```
This is effectively importing the module in the same way that `import my_module` will 
do, with the only difference of it being available as `mm`. It can also be used 
when utilising `from` with similar effects:

```python
from calculator import Subtract as Minus
```

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6019#module-loading?utm_source=jba&utm_medium=jba_courses_links).

### Task
Import the `Calculator` class from `calculator` and create an instance of this class. Remember how to access it correctly in 
this case.


<div class="hint">Note: The <code>Calculator</code> class should be called without a prefix because you 
imported it directly.</div>

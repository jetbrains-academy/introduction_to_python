## from import

One form of the import statement imports names `from` a module directly. This way, you 
can use the imported name without the `module_name` prefix.  For example:

```python
from calculator import Add

calc = Add()    # name `Calculator` used directly without prefix `calculator`
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

Import the `hello` function from `my_module` as `hey` and call it to print your name.

<div class='hint'>Use syntax such as <code>from some_module import some_func as func</code>.</div>
<div class="hint">Note: The <code>hey</code> function should be called without a prefix. The function expects
one string argument.</div>

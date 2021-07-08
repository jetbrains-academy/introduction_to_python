## Built-in modules

Python comes with a [library of standard modules](https://docs.python.org/3/library/). 

Some modules are built into the interpreter; these provide access to operations that are 
not part of the core of the language but are nevertheless built in, either for efficiency 
or to provide access to operating system primitives, such as system calls.  
One particular module deserves some attention: `sys`, which is built into every Python 
interpreter. The variables `sys.ps1` and `sys.ps2` define the strings used as primary and 
secondary prompts if the interpreter is in the interactive mode:

```text
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
```

The variable `sys.path` is a list of strings that determines the interpreter’s search path 
for modules: see what it prints for you when you run the code of the task.

Remember that you can use &shortcut:CodeCompletion; after a dot (.) to explore available 
methods of a module. You can read more about standard modules <a href="https://docs.python.org/3/tutorial/modules.html#standard-modules">here</a>.
  
Print the current date using an imported built-in module `datetime`.  

<div class='hint'>Use the <code>datetime.datetime.today()</code> function.</div>

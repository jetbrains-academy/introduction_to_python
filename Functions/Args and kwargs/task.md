## Args and kwargs

When a final formal parameter of the form `**name` is present, it receives a dictionary 
(see [Data Structures — Dictionaries ](course://Data structures/Dictionaries)) containing 
all keyword arguments except for those corresponding 
to a formal parameter. This may be combined with a formal parameter of the form `*name` which 
receives a tuple containing any number of positional arguments beyond the formal parameter list 
(`*name` must occur before `**name`). For example, if we define a function like the one in the 
code editor, it could be called as shown in call 1, which would print:
```text
-- Do you know how to get to the Library ?
-- I'm sorry, I am not from here, no idea about the Library
Do you at least have a cigar, sir?
Sure, help yourself.
----------------------------------------
lost_person : old banker
other_guy : street clown
scene : in a park
```
This function can be called with an arbitrary number of arguments. These arguments will be wrapped 
up in a tuple (see [Tuples](course://Data structures/Tuples)). Before the variable number of arguments, zero or 
more normal arguments may occur; in our case there's one – `place`. Any formal parameters that occur 
after the `*args` parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords 
rather than positional arguments. Another way to call this function is shown in call 2, and it will give 
us the same output.

In the code editor, modify the code below the `cat()` function so that it prints 
the following:
```text
-- This cat would eat if you gave it anything
-- Lovely fur, the Maine Coon
-- It's fat !
IT IS TOO FAT.
YOU ARE FEEDING YOUR CAT TOO MUCH.
```
<div class="hint">Remember to unpack extra positional arguments with <code>*</code>.</div>

<div class="hint">Remember to unpack keyword arguments with <code>**</code>.</div>

<div class="hint">Do not forget to provide the value for the formal parameter <code>food</code>.</div>



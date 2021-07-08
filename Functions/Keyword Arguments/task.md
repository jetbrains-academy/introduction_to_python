## Keyword Arguments

We already hinted that functions can also be called using keyword arguments of the form `kwarg=value`. For 
instance, the function `cat()`, which we defined for you,
accepts one required argument (`food`) and three optional arguments (`state`, `action`, and `breed`). 
It can be called in any of the following ways (you can try them all out):

```python
cat('chicken')                     # 1 positional argument
cat(food='chicken')                # 1 keyword argument
cat(food='fish', action='bite')    # 2 keyword arguments
cat(action='bite', food='fish')    # 2 keyword arguments
cat('beef', 'happy', 'hiss')       # 3 positional arguments
cat('a hug', state='purrring')     # 1 positional, 1 keyword
```
In a function call, keyword arguments must follow positional arguments. All the keyword 
arguments passed must match one of the arguments accepted by the function (e.g., `book` is not a valid 
argument for the `cat` function), and their order is not important. This also includes non-optional 
arguments (e.g., `cat(food='fish')` is valid too). No argument may receive a value more than once.
All the following calls would be invalid:

```python
cat()                              # required argument missing
cat(food='fish', 'dead')           # positional argument after a keyword argument
cat('veggies', food='nothing')     # duplicate value for the same argument
cat(actor='Johnny Depp')           # unknown keyword argument
```
In the editor, complete the function call  with arguments so that it prints the following:
```text
-- This cat wouldn't growl if you gave it soup
-- Lovely fur, the Sphinx
-- It's still hungry!
```

<div class="hint">For keyword arguments, use syntax such as <code>state='asleep'</code>.</div>
<div class="hint">The required argument <code>food</code> has to be in the first position, unless you supply it as a keyword argument.</div>
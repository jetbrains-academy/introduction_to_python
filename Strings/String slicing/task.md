## Slicing

Slicing is used to extract multiple characters (a substring) from a string. 
Its syntax is similar to that of indexing, but instead of just one index you use 
two indices (numbers) separated by a colon, e.g., `str[ind1:ind2]`. These two 
indices correspond to the start and the end of the substring. Note that the symbol 
with the index `ind1` will be included, while the symbol with the index `ind2` – won't.

Here's a visual on how slicing works in Python:

```text
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

##### Example
<pre><code>
str[start:end] # items start through end-1
str[start:]    # items start through the rest of the array
str[:end]      # items from the beginning through end-1
str[:]         # a copy of the whole array
</code></pre>

Use slicing to get `"Python"` from the `monty_python` variable.  

<div class='hint'>You can leave one of the indices empty.</div>

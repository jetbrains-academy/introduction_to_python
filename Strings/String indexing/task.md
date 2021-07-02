## String indexing

You can access a character in a string if you know its position. For example, 
`str[index]` will yield the character at position `index` in the string `str`.
Note that string indexing always starts at `0`. `index` raises `ValueError` 
when `x` is not found in the string.

Indices may also be negative numbers if you need to start counting from the right 
(i.e., from the end of your string). 
Note that since `-0` is the same as `0` , negative indices start from `-1`.  
  
Use the index operator to get the letter `"P"` from `"Python"` .  

<div class="hint">Note that indices start with 0.</div>

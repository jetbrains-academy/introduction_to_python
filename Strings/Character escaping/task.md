## Character escaping

Backslash is used to escape special symbols, such as single or double quotation marks, 
for example, `"It\'s me"` or `"She said \"Hello\""`. If you need to actually type the <code>\\</code>
character as part of your string, you will need to escape it too. For example, here's how 
you print a single backslash:

```python
print('\\')
```

The special symbol `'\n'` is used to add a line break to a string, while `'\t'` means tabulation.

Quotes have special meanings, and they can be escaped with a backslash too. 
If you need to print quotes inside a string, use a different kind of quotes: single quotation 
marks may be used in a double-quoted string without escaping, and vice versa. Also, as a side note, it is a good 
idea to pick your favorite kind of quotes and use them consistently.

You can learn more about escaping from <a href="https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals">this section</a> of Python Documentation.  

Print out the following text using one string:  
```text
The name of this ice-cream is "Sweet'n'Tasty"  
```


<div class='hint'>Use the backslash to escape quotes.</div>

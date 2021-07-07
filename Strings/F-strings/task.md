## Formatted string literals

A formatted string literal, or an f-string, is a string literal that is prefixed 
with 'f' or 'F'. These strings may contain replacement fields, which are 
expressions delimited by curly braces `{}`. 

The parts of the string outside curly braces are treated literally. 
Escape sequences are decoded like in ordinary string literals.
Replacement expressions can contain line breaks (e.g., in triple-quoted strings), 
but they cannot contain comments. Each expression is evaluated in the context 
where the formatted string literal appears, in order from left to right.

Here are some examples:
```python
name = "Fred"
f"He said his name is {name}."
```
```text
'He said his name is Fred.'
```

There are more fancy things you can do in f-strings, for example:
```python
f"{name.lower()} is funny."
```

```text
'fred is funny.'
```
For more information about formatted string literals you can refer to <a href="https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals">Python Docs</a>.

Try creating an f-string yourself. Also try running the code to see what it prints.

<div class="hint">The value assigned to the <code>name</code> variable has to be a string, so it needs to be in quotes, 
like so: <code>'Max'</code>.</div>


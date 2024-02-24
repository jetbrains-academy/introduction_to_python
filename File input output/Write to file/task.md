## Write to file

As we already mentioned, if you use `'w'` as the second argument in `open()`, the file opens for 
writing only. A new empty file will be created. If another file with the same name already exists, it 
will be erased. If you want to add some content to an existing file, you should use the `'a'` 
(append) modifier.  
  
Another file object method, `f.write(string)`, writes the contents of a <i>string</i> to the file, returning the 
number of characters written.

```python
f.write('This is a test\n')
```
```text
15
```
Other types of objects in text mode need to be converted into a string first:
```python
value = ('the answer', 42)
s = str(value)  # convert the tuple into string
f.write(s)
```
```python
18
```
Where the specified text will be inserted in the file depends on the file mode (`'a'` vs `'w'`).

`'a'`:  the text will be inserted at the end of the file.

`'w'`: the file will be emptied before the text will be inserted at the beginning.

If you want to include a symbol such as a line break, into your string (to start from a new line),
add it with a `+`:
```python
f.write('\n' + 'string,' + ' ' + 'another string')
```
This will add a new line and write `'string, another string'`.

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/8334?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, **append** one new line to `output.txt` with all elements from the `zoo` list separated by `' and '`. 
Use the <code>' and '.join(lst)</code> syntax to join the list elements into the required string. Afterwards, 
append another line with the `number` to the same output file.

<div class='hint'>Use the <code>'a'</code> modifier to append lines at the end of the file.</div>
<div class='hint'>Use the <code>write()</code> method.</div>
<div class='hint'>Convert <code>number</code> into a string before writing.</div>
<div class="hint">Add <code>\n</code> at the beginning of each string to write, so that it ends up on a separate line.</div>

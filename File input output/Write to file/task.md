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

In the code editor, add all elements from the `zoo` list to "output.txt" so that the output is added from
a new line and the elements are separated by `' and '`. Use the <code>' and '.join(lst)</code> syntax to 
join the list elements into the required string. Afterwards, add `number` to the same output file.

<div class='hint'>Use the <code>'a'</code> modifier to append lines at the end of the file.</div>
<div class='hint'>Use the <code>write()</code> method.</div>
<div class='hint'>Convert <code>number</code> into a string before writing.</div>
<div class="hint">Add <code>\n</code> at the beginning of each string to write so that it's written as a separate line.</div>



## What's next?

Now, once you have mastered the basics of Python, we bet that you’re wondering what to do next. 
We recommend checking out [JetBrains Academy](https://hi.hyperskill.org?utm_source=ide&utm_medium=ide&utm_campaign=ide&utm_content=last-task). 
Here are several reasons to try JetBrains Academy now:

- At the moment, 37 Python projects and 348 topics are available for learning, and the number keeps growing.
  Other programming languages, such as Kotlin and Java, are also available.
- Projects of varying difficulty levels provide a flexible learning experience for all.
- Comprehensive learning tracks are augmented with a detailed [Knowledge Map](https://hyperskill.org/knowledge-map?utm_source=ide&utm_medium=ide&utm_campaign=ide&utm_content=last-task).
- Learn anywhere: you can start learning on your tablet or mobile phone via a browser and continue on your 
  laptop or PC; you can even build the projects [right in your IDE](https://hyperskill.org/plugin#python?utm_source=ide&utm_medium=ide&utm_campaign=ide&utm_content=last-task).

Join JetBrains Academy [here](https://hyperskill.org/onboarding?track=python&utm_source=ide&utm_medium=ide&utm_campaign=ide&utm_content=last-task) and try it yourself!

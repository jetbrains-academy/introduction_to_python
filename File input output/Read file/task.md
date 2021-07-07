## Read file


To read a file’s contents, you can call `f.read(size)`, which reads some quantity of data and returns it as 
a string. When size is omitted or negative, the entire contents of the file will be read and returned.

```python
with open('somefile.txt') as f:
    print(f.read())
```
```text
Here's everything that's in the file.\n
```
<i>**Note**: there will be a problem if the file is twice as large as your machine’s memory.</i>


`f.readline()` reads a single line from the file; a newline character (`\n`) is left at the end of the 
string and is only omitted on the last line of the file if the file doesn’t end in a newline. If `f.readline()` 
returns an empty string, the end of the file has been reached, while a blank line is represented by `\n`, 
a string containing only a single newline.

```python
f.readline()
```
```text
'This is the first line of the file.\n'
```
```python
f.readline()
```
```text
'Second line of the file\n'
```
```python
f.readline()
```
```text
''
``` 
For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and 
makes the code simple:
```python
for line in f:
    print(line)
```
```text
This is the first line of the file.
Second line of the file
```

If you want to read all the lines of a file in a list, you can also use `list(f)` or `f.readlines()`.


For more details, check out the section [Methods of File Objects](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) in Python Tutorial.


Print the contents of "input.txt" to output by iterating over the lines of the file and printing each one.
Then print only the first line of "input1.txt".

<div class="hint">Loop over the file object as in the example in the task description.</div>
<div class='hint'>Use the <code>print</code> function.</div>
<div class='hint'>Use the <code>readline()</code> method to print a single line.</div>

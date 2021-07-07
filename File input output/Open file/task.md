## Open file
Python has a number of built-in functions to read and write information to a file on your computer.

`open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`:
```python
f = open('somefile.txt', 'w')
```
The first argument is a string containing the filename. The second argument is another string containing
a few characters describing the way in which the file will be used. It can be `'r'` if the file
will only be read, `'w'` – for writing only (an already existing file with the same name will be erased), and
`'a'` opens the file for appending – any data written to the file is added to its end.
`'r+'` opens the file for both reading and writing. The mode argument is optional; `'r'` will be assumed
if it’s omitted.

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the
file is properly closed after the code suite finishes.

```python
with open('somefile.txt') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
```
```text
True
```
**Important**: If you’re not using the `with` keyword, then you should call `f.close()` to close the file and 
free up any system resources used by it. You cannot use the file object after it is closed, whether by a `with` statement or by calling `f.close()`.

In the code editor, open the file `input1.txt` in read mode properly using the `with` statement. Check out the
name that is used for the file in the later code and use it. Afterwards, close the output file using the 
`close()` method.

<div class="hint">Supply the <code>r</code> argument to the method <code>open()</code>,
just for the sake of practicing!</div>

## Comments

Comments in Python start with the hash character (`#`) and a single space, 
and they extend to the end of the physical line. You can use &shortcut:CommentByLineComment; to comment 
or uncomment the whole line or a block of code in PyCharm.  


Always make a priority of keeping the comments up-to-date when the code changes!
Comments that contradict the code are worse than no comments.
Also, they are unnecessary and in fact quite distracting if they state the obvious. Don't do this:

```python
x = x + 1                 # Increment x
```

Comments should be complete sentences. The first word should be capitalized, 
unless it is an identifier that begins with a lower case letter. Ensure that 
your comments are clear and easily understandable to other people. 

#### Block Comments

Block comments generally apply to some (or all) code that follows them, and 
are indented to the same level as that code. 

#### Inline Comments
Use inline comments sparingly. An inline comment is a comment on the 
same line as a statement. Inline comments should be separated by at least two spaces from the statement.

You can read more about proper commenting in <a href="https://www.python.org/dev/peps/pep-0008/#comments">PEP 8 – Style Guide for Python Code</a>. 
  
You can also comment a line or a block of code if you don't want to delete it, but it's not needed at the moment. 

For more structured and detailed information, you can refer to [this Hyperskill knowledge base page](https://hyperskill.org/learn/step/6081?utm_source=jba&utm_medium=jba_courses_links).

### Task
In the code editor, comment the line with the `print` statement that says it should not be printed. 
See how the code is not highlighted anymore.

<div class="hint">
  Add a <code>#</code> and a space before that <code>print</code> statement. Leave everything else as is.
</div>

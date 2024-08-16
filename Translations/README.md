## Translated the "Description" of "Introduction to Python" into Japanese:

### description:

The explanation displayed is in English. I translated it into Japanese to make it easier for people living in Japan to learn Python.

---

### Setup procedure:

#### 1. Install the following plug-in in "PyCharm":

- "Edu Tools"  
- "Japanese Language Pack"

#### 2. In PyCharm's "Courses" tab, select "Introduction to Python" and click "Start":

-> A "~/PycharmProjects/'Introduction to Python'/" folder will be created.

This should have already been done.

#### 3. Save the original file just in case:

```
$ cp -r ~/PycharmProjects ~/PycharmProjects-ORG
```

#### 4. Check the files used for work:

Suppose you have attachments in the following folders:

```
$ cd ~/PycharmProjects/'Introduction to Python'/Translations/
$ ls -1
Delete-md-File.sh
README-ja.md
README.md
ja.patch
screenshot-ja.jpg
```

#### 5. Set the shell script to be executable:

```
$ chmod +x ./Delete-md-File.sh
```

#### 6. Run a shell script that deletes the target file:

```
$ cd ~/PycharmProjects/'Introduction to Python'/
$ ./Translations/Delete-md-File.sh
```

-> Avoid errors when applying patch files:  
"Hunk #1 FAILED at 1 (different line endings)."

And make it a new file to make it easier to apply.

#### 7. Apply patch file:

```
$ patch -p1 <Translations/ja.patch
```

-> A new md file is created in each file hierarchy.

#### 8. Start and check:

Double-click on the issue name in the tree on the left to see the translated description.

---

### Attachment:

(1). "README.md" : Setup procedure.  
(2). "README-ja.md" : Setup procedure (Japanese version)  
(3). "screenshot-ja.jpg" : Screen using "Introduction to Python" translated into Japanese  
(4). "Delete-md-File.sh"  : Shell script that deletes the target file  
(5). "ja.patch"  : patch file:


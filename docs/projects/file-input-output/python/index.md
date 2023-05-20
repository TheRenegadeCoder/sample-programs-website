---
title: File Input Output in Python
layout: default
last-modified: 2020-05-02
featured-imaged: file-input-output-in-every-language.jpg
tags: [python, file-input-output]
authors:
  - noah11012

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
def write_file():
    try:
        with open("output.txt", "w") as out:
            out.write("Hi! I'm a line of text in this file!\n")
            out.write("Me, too!\n")
    except OSError as e:
        print(f"Cannot open file: {e}")
        return


def read_file():
    try:
        with open("output.txt", "r") as in_file:
            for line in in_file:
                print(line.strip())
    except OSError as e:
        print(f"Cannot open file to read: {e}")
        return


if __name__ == '__main__':
    write_file()
    read_file()
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Python](https://sampleprograms.io/languages/python) was written by:

- Ganesh Naik
- Jeremy Grifski
- Noah Nichols

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 22:17:17. The solution was first committed on Sep 12 2018 13:00:03. As a result, documentation below may be outdated.

## How to Implement the Solution

We'll first present the solution in its entirety. Then, we'll go over the code
line by line.

Afterward, we'll take a look at how to run the solution.

### Writing to a File

As you may have noticed above, our file writing procedure has been broken out
into its own function:

```python
def write_file():
    try:
        with open("output.txt", "w") as out:
            out.write("Hi! I'm a line of text in this file!\n")
            out.write("Me, too!\n")
    except OSError as e:
        print(f"Cannot open file: {e}")
        return
```

First, we setup up a `try/except` block to catch any exceptions that might occur
when we want to open a file:

```python
try:
    with open("output.txt", "w") as out:
        ...
except OSError as e:
    print("Cannot open file: {}", e)
```

The Python documentation tells us if `open()` fails to create a new file, it will
raise an `OSError` exception. If we do get an exception, we will exit the method.

Next, if no exceptions occurred, we can now write to the file using the `write()`
method:

```python
out.write("Hi! I'm a line of text in this file!\n")
out.write("Me, too!\n")
```

As we can see, we attempt to output a couple of lines to the text file. The
[with][1] statement sets up a context that will automatically close the file
when the context is exited.

### Reading From a File

After we write to a file, we can read back from that file. Naturally, we've
broken the reading procedure into its own function:

```python
    try:
        with open("output.txt", "r") as in_file:
            for line in in_file:
                print(line.strip())
    except OSError as e:
        print(f"Cannot open file to read: {e}")
        return
```

Just like when we were opening the file for writing purposes, we surround the
code that could potentially raise exceptions in a `try/except` block:

```python
try:
    with open("output.txt", "r") as in_file:
        ...
except OSError as e:
    print(f"Cannot open file to read: {e}")
    return
```

If an exception occurs, we report the error and exit the function.

Next, we have a while loop that iterates over each line in the file:

```python
for line in in_file:
    print(line.strip())
```

As we can see, the loop performs some basic processing before we print the line
out onto the screen. When we get a line from the file, we also get the newline.
If we print it with the newline we print an extra empty line because print 
automatically adds a newline by default. To fix this problem we use `strip()` to
strip away any newlines at the end of the line. This loop will end when we reach
EOF (end of file).

The [with][1] statement sets up a context that will automatically close the file
when the context is exited.

### The Main Function

All of this code would be useless if we didn't execute it somewhere. Thankfully,
we can drop everything into the main function:

```python
if __name__ == '__main__':
    write_file()
    read_file()
```

And, that's it! We've conquered File IO in Python.

[1]: https://docs.python.org/3/reference/compound_stmts.html#with


## How to Run the Solution

As usual, you're free to use an online Python interpreter such as the one on
Repl and run the solution there. Alternatively, if you have a Python interpreter
installed on your machine, you can use the following command:

```console
python file-input-output.py
```

After you execute this command, you should be able to find a nearby `output.txt`
file containing the arbitrary text we used earlier. If so, you've successfully
run the program.

---

title: Reverse a String in Python
layout: default
last-modified: 2020-05-02
featured-image: reverse-a-string-in-python.jpg
tags: [python, reverse-a-string]
authors:
  - the_renegade_coder

---

Welcome to the Reverse String in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
import sys

if len(sys.argv) > 1:
    print(sys.argv[1][::-1])

```

## How to Implement the Solution

Let�s start by looking at the complete algorithm to reverse a string in Python:

```python
import sys
if len(sys.argv) > 1:
    print(sys.argv[1][::-1])
```

As we can see, we can write a script to reverse a string in about three lines
of code. In the following sections, we�ll take a look at a breakdown of each of
these lines.

### The Python `sys` Library

In the first line of code, we�ll notice that we�re importing the built-in sys
library:

```python
import sys
```

If you�re unfamiliar with this library, basically it contains functions for
interacting directly with the interpreter during runtime.

In our case, we�re leveraging the library to access the command line. From the
command line, we can get our string that we�re going to reverse.

### The Conditional

After we�ve imported our sys library, this script runs a bit of a sanity check:

```python
if len(sys.argv) > 1:
```

If we recall from the previous section, we found out that `sys` gives us access to
the command line. We can get the array of command line arguments using `argv`.
According to Python documentation, `argv` is the list of command line arguments.

With that in mind, it�s clear that we�re just verifying its length. But, why
aren�t we just checking to see if the list is empty? That would probably be
more efficient and more explicit. Well, as it turns out, the interpreter stores
the script name as the first argument, so `argv` will always contain at least one
element.

If we put all that information together, we�ll notice that we only branch if the
list of command line arguments contains more than one item. If it does, we know
the user has passed us some string.

### The Slice & Print

Our last line is a bit terse, but we can handle it:

```python
print(sys.argv[1][::-1])
```

The first thing to note is the print statement. We�ll probably remember that
from our Hello World experience, so no need to dig into that much deeper.

Inside the print statement, we have quite a bit of syntax. First, we access our
command line arguments again using sys.argv. However, this time we�re trying to
access one of the items using an index of one. Like many languages, Python list
indices start from zero, so clearly we�re trying to access our string for reversal.

After that, we�ll notice another piece of interesting syntax: [::-1]. It looks
sort of like list access, but it has colons and a negative value. As it turns
out, that syntax is called a slice. Typically, slices are used to get a subset
of an iterable. For instance, if I wanted the first four characters of a string,
I could do the following:

```python
myString = "Hello, World!"
print(myString[:4])  # Prints "Hell"
```

Okay, maybe that�s not a family friendly example, but you get the idea.

Now, with a single colon, we can slice between any two indices. With a second
colon, we can declare the step. For example, maybe we want every other character
in a string:

```python
myString = "Hello, World!"
print(myString[::2])  # Prints "Hlo ol!"
```

As an added wrinkle, we can step backwards through the string using a negative
value. That�s exactly how we reverse the string in our example.

So, let�s put it all together. We get our string off the command line, take a
slice of it backwards, and print the result. How cool is that?


## How to Run the Solution

To run the Reverse a String in Python program, grab a copy of the Python file
from GitHub. After that, get the latest version of Python. Now, all you have to
do is run the following from the command line:

```console
python reverse-string.py "Hello, World!"
```

Alternatively, you can always copy the source code into an online Python
interpreter. Just make sure you pass some input to your script before you run
it.

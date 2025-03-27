---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-03-15
featured-image: hello-world-in-python.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- python
title: Hello World in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/python/how-to-implement-the-solution.md
- sources/programs/hello-world/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
print('Hello, World!')

```

{% endraw %}

Hello World in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

I chose Python to start as it has probably the easiest and most readable 
Hello World implementation in the realm of programming languages.

We don't even have to compile anything. If we're in 
the interpreter, we'll print right away. Otherwise, we can easily call the 
script from the command line to get our result.

As you can probably imagine, this code works because Python has a built-in 
function called *print*. By passing that function a string, the interpreter 
is able to call the Python libraries that make the print possible.


## How to Run the Solution

If we want to run this program, we should probably download a copy of
[Hello World in Python][1]. After that, we should make sure we have the
[latest Python interpreter][2]. From there, we can simply run the following
command in the terminal:

```console
python hello-world.py
```

Alternatively, we can copy the solution into an [online Python interpreter][3]
and hit run.

[1]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/python/hello_world.py
[2]: https://www.python.org/downloads/
[3]: https://www.online-python.com/

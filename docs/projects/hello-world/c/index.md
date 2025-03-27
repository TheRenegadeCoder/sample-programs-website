---
authors:
- "Christoph B\xF6hmwalder"
- Jeremy Griffith
- Jeremy Grifski
- Johnny Fang
- rzuckerm
date: 2018-03-15
featured-image: hello-world-in-c.jpg
last-modified: 2023-05-15
layout: default
tags:
- c
- hello-world
title: Hello World in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/c/how-to-implement-the-solution.md
- sources/programs/hello-world/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>

int main()
{
   puts("Hello, World!");
   return 0;
}

```

{% endraw %}

Hello World in [C](https://sampleprograms.io/languages/c) was written by:

- Christoph Böhmwalder
- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- Johnny Fang
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Since C predates both Java and Python, the syntax is naturally a bit archaic.
That said, you'll find that the syntax for Hello World in C is still easier to
understand than Java.

At the top, we'll notice an `include` statement. Basically, this statement copies
in functionality from the standard IO library of C. This includes the `printf`
functionality we'll need to actually write our string to the command line.

Like Java, we'll notice that we have a `main` function. In C, the `main` function is
much simpler. In fact, we don't even have classes in C, so we don't have to bother
with that extra layer of abstraction. Instead, we can define the `main` function
directly. Again, we can only define one of these per program.

Inside the `main` function, we'll find our usual call to print. However, in C,
we use `printf` which allows us to format strings as well.

Finally, we'll notice that we return zero. That's because the `main` function is
like any other function, so it has a return type. In this case, the return type
is an integer, and that integer is used to indicate status codes. A status code
of zero means no errors occurred.


## How to Run the Solution

Now, if we want to run the solution, we'll need to [get a hold of a C compiler][1].
In addition, we'll probably want to [get a copy of Hello World in C][2]. With both
prerequisites out of the way, all we have to do is navigate to our file and run
the following commands from the command line:

```console
gcc -o hello-world hello-world.c
./hello-world
```

Of course, these are Unix/Linux instructions. If we're on Windows, it may be easier
to take advantage of an [online C compiler][3]. Alternatively, we can leverage a tool
like [MinGW][4].

[1]: https://gcc.gnu.org/
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/c/c/hello-world.c
[3]: https://www.programiz.com/c-programming/online-compiler/
[4]: https://www.mingw-w64.org/

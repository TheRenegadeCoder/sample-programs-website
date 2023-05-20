---
title: Hello World in C
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-c.jpg
tags: [c, hello-world]
authors:
  - the_renegade_coder

---

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

[Hello World](https://sampleprograms.io/projects/hello-world) in [C](https://sampleprograms.io/languages/c) was written by:

- Christoph Böhmwalder
- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jul 24 2018 11:02:56. The solution was first committed on Mar 15 2018 20:27:08. As a result, documentation below may be outdated.

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

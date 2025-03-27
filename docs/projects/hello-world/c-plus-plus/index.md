---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-03-21
featured-image: hello-world-in-c-plus-plus.jpg
last-modified: 2023-05-15
layout: default
tags:
- c-plus-plus
- hello-world
title: Hello World in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/hello-world/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello, World!";
    return 0;
}

```

{% endraw %}

Hello World in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Griffith
- Jeremy Grifski

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Even though C++ was built on C, the implementation of Hello World in 
C++ is slightly different.

It appears this implementation of Hello World may be competing with 
Java for hardest to learn. But at any rate, let's break it down.

Once again, the first line is an `include` statement. Here, we're including 
the IO stream code in our solution. This is how we gain access to the 
IO objects like `cout`.

Next, we gain access to the `std` namespace which basically allows us to 
shorten `std::cout` to `cout`. It's really just a style thing that eliminates 
a lot of verbosity that you might get with other languages like Java. 
Of course, if another namespace also has a `cout`, we'll run into problems.

After that, we make a `main` method as usual. This is exactly the same as 
C, so I won't bother explaining the return type bit again.

Finally, we write our string to the `cout` stream. The syntax is a bit 
strange, but basically we can imagine that the Hello World string is 
inserted into the `cout` stream. In fact, the double-arrow operator is 
the insertion operator, and it has some fun properties. For instance, 
the operator can be chained together, but that's a topic for another time.


## How to Run the Solution

Perhaps the easiest way to run the solution is to leverage the [online gdb compiler][1].

Alternatively, you can try to run the C++ code in a similar way described 
in the last article. Honestly, it's pretty easy to write and run C/C++ code 
on most platforms:

```console
gcc -o hello-world hello-world.cpp
./hello-world
```

Unfortunately, Windows pretty much requires the use of Visual Studio. So, 
instead of sharing platform specific directions, I'll fallback on my online 
compiler recommendation.

[1]: https://www.onlinegdb.com/online_c++_compiler

---
authors:
- Jeremy Grifski
- rzuckerm
date: 2022-04-28
featured-image: hello-world-in-c-star.jpg
last-modified: 2023-12-09
layout: default
tags:
- c-star
- hello-world
title: Hello World in C*
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/c-star/how-to-implement-the-solution.md
- sources/programs/hello-world/c-star/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C\*](https://sampleprograms.io/languages/c-star) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c\*
void main()
{
    println("Hello, World!");
}

```

{% endraw %}

Hello World in [C\*](https://sampleprograms.io/languages/c-star) was written by:

- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At long last, here's Hello World in C*.

As we can see, Hello World in C* looks similar to C. That said, C*
is a superset of C, so this shouldn't be too much of a surprise. At any rate,
let's dig in.

Unlike C, there is no `include` statement. As far as I can tell, the language
does not actually have an `include` statement or header files. Somehow, the
compiler know where to pull the definition for standard libraries.

Next, we have our usual `main` function declaration which serves as the drop in
function for our program. We should be used to seeing this convention since it's
common in the popular industrial languages like C++ and Java.

Finally, we make a call to `println` which is a special print function that outputs
the specified string with a newline character. Of course, all we're going to pass
to it is the "Hello, World!" string. And, that's it!


## How to Run the Solution

The compiler source can be found in the [C* GitHub repository][1]. To build it,
just follow the [build from source instructions][2] for your particular OS.
Once, you've built the compiler, download a copy of the [Hello World in C* sample][3].
Then, build and run the program like this:

```
cx -o hello-world hello-world.cx
./hello-world
```

[1]: https://github.com/cx-language/cx
[2]: https://github.com/cx-language/cx#building-from-source
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/c/c-star/hello-world.cx

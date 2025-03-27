---
authors:
- Jeremy Grifski
- rzuckerm
date: 2022-04-28
featured-image: hello-world-in-koka.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- koka
title: Hello World in Koka
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/koka/how-to-implement-the-solution.md
- sources/programs/hello-world/koka/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Koka](https://sampleprograms.io/languages/koka) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```koka
fun main() 
{
    println("Hello, World!")
}

```

{% endraw %}

Hello World in [Koka](https://sampleprograms.io/languages/koka) was written by:

- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Now, let's see how we can print a simple "Hello World" in Koka.

Just like many other programming languages, the `main` function is the starting
point of the code execution. To print, we use `println`, a built-in method that
prints a given string or variable to the console.

Like many of the high-level language implementations in this series, this one
wasn't too bad. Wanna try it out? Check out this [online Koka editor][1].

[1]: https://tio.run/#koka


## How to Run the Solution

If you want to run Koka at your local machine, you can always install the [Koka compiler][2]
and try the snippet locally. Then, run the following:

```console
koka hello_world.kk
```

Also, you can check out the [Koka the documentation][3].

[2]: https://koka-lang.github.io/koka/doc/index.html#install
[3]: https://koka-lang.github.io/koka/doc/book.html

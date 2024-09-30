---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-20
featured-image: hello-world-in-wren.jpg
last-modified: 2023-05-16
layout: default
tags:
- hello-world
- wren
title: Hello World in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/wren/how-to-implement-the-solution.md
- sources/programs/hello-world/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
System.print("Hello, World!")

```

{% endraw %}

Hello World in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Personally, I'm getting hints of Java and
Python here just in terms of syntax.

At any rate, let's break it down. Obviously, we only have
one line, but it's at least a little more interesting than
most scripting languages.

For starters, we have the built-in `System` class. This class
comes with the core module along with a few other goodies like
`String`, `Sequence`, `Fiber`, and `Bool`.

Now, one of the functions of `System` is `print`. Obviously, `print`
writes text to standard output. But, I find Wren's `print`
functionality particularly interesting because it's similar to
Java. In fact, it accepts any object as input. If the input is
not a `String`, `print` will convert it to a `String` using the
`toString` functionality, a method available to all objects.

So, basically we call the static method print of the `System` class
which prints the input to the user. How cool is that?


## How to Run the Solution

You can [download a copy of Wren][1] to your local machine, grab a copy of
[Hello World in Wren][2], and then run this:

```
wren_cli hello-world.wren
```

Alternatively, you can use an [online Wren interpreter][3].

[1]: https://github.com/wren-lang/wren-cli/releases
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/w/wren/hello-world.wren
[3]: https://wren.io/try/

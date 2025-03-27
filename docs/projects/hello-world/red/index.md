---
authors:
- Jeremy Griffith
- Jeremy Grifski
- Johnny Fang
- rzuckerm
- shubhragupta-code
date: 2018-04-20
featured-image: hello-world-in-red.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- red
title: Hello World in Red
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/red/how-to-implement-the-solution.md
- sources/programs/hello-world/red/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Red](https://sampleprograms.io/languages/red) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```red
Red [Title: "Hello World in Red"]

print "Hello, World!"

```

{% endraw %}

Hello World in [Red](https://sampleprograms.io/languages/red) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- Johnny Fang
- rzuckerm
- shubhragupta-code

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's get right to our implementation of Hello World in Red.

Honestly, this is about the weirdest syntax I've ever seen, so I really
had to dig into the docs.

[According to Helpin'Red][1], the first line in our solution is the header,
and it's absolutely necessary for all scripts. The header is composed of two
parts: the `Red` keyword and the block..

Now, every script will have the `Red` keyword. As for the block, well, that
will vary per script. Honestly, the information in that block is largely
optional, but it can be used to declare script information such as a title,
a description, a version, and an author. In this case, I simply gave the
script a title.

In addition to arbitrary information, the first block can also be used to
import libraries. For example, we could have implemented Hello World in
Red as a GUI:

```red
Red [needs: 'view]

view [
  text "Hello, World!"
]
```

Here, we use the header block to import the graphics view library. Then,
we use that library to display a window containing "Hello, World!"

At any rate, the last line in our original implementation clearly prints
"Hello, World!" to the user. We've seen this plenty of times already so
no need to dig into it.

[1]: https://helpin.red/Helloworld-runandcompile.html


## How to Run the Solution

If we're looking to run this solution, perhaps the easiest way to do so
is to [download the latest Red toolchain][2]. Of course, we'll also want
to grab a copy of the [Hello World script from GitHub][3].

Now, drop both of those files in the same folder and run the following:

```console
red hello-world.red
```

If you're a Windows user, you may need to call the executable directly.

In addition, we can compile our script using the following command:

```console
red -c hello-world.red
```

At this point, I would usually share some online editor you could use to test
code, but Red doesn't appear to have one. If one exists, let me know in
the comments.

[2]: https://www.red-lang.org/p/download.html
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/r/red/hello-world.red


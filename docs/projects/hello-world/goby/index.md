---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-20
featured-image: hello-world-in-goby.jpg
last-modified: 2023-05-15
layout: default
tags:
- goby
- hello-world
title: Hello World in Goby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/goby/how-to-implement-the-solution.md
- sources/programs/hello-world/goby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Goby](https://sampleprograms.io/languages/goby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```goby
puts("Hello, World!")

```

{% endraw %}

Hello World in [Goby](https://sampleprograms.io/languages/goby) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

As seen many times in this collection, Hello World in Goby is actually
really simple. In total, it's one line of code which looks a lot like
Ruby.

Alternatively, we can leave out the parentheses:

```goby
puts "Hello, World!"
```

Naturally, `puts` writes the "Hello, World!" string to the user, and that's it!


## How to Run the Solution

To run this solution, we can take advantage of the samplerunner script
included in the [Sample Programs repo][2]. If our system is setup
correctly, the following command should get the job done:

```shell
glotter run -s hello-world.gb
```

Alternatively, we may want to get a copy of the Goby interpreter. [According
to the documentation][1], there are a few ways to do that, but we won't 
dig into that now.

Unlike many other languages in this collection, Goby does not have an online 
interpreter at this time.

[1]: https://github.com/goby-lang/goby
[2]: https://github.com/TheRenegadeCoder/sample-programs

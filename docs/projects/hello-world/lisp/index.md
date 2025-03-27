---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-08
featured-image: hello-world-in-lisp.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- lisp
title: Hello World in Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/lisp/how-to-implement-the-solution.md
- sources/programs/hello-world/lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(format t "Hello, World!")
```

{% endraw %}

Hello World in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Unfortunately, Lisp has many flavors which means the following implementation 
of Hello World will likely only be applicable to handful of those flavors:

That said, I'm happy to dig into this implementation of Hello World in Lisp.

First things first, we have the `format` keyword. In Common Lisp, `forma`t is 
basically the equivalent to `printf` in C. It basically takes some string and 
outputs it to some destination.

That brings us to this mysterious letter `t`. According to gigamonkeys, `t` is 
actually the destination of the output. More specifically, `t` indicates standard 
output. Another option is `NIL` which causes the string to be returned.

Finally, we have our Hello World string. This is obviously what gets printed 
to standard output.


## How to Run the Solution

If we want to try it ourselves, we can copy the code above into an
[online Common Lisp compiler][1]. The one I linked is in CLISP, but it gets the job done.

Alternatively, as mentioned before, we can download a copy of
[Steel Bank Common Lisp][2] as well as a [copy of the solution][3].
Assuming SBCL is in the path, we can run a lisp file like a script as follows:

```console
sbcl --script hello-world.lsp
```

And, that should produce the "Hello, World!" string on the command line.

[1]: https://ideone.com/l/common-lisp-clisp
[2]: https://www.sbcl.org/platform-table.html
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/l/lisp/hello-world.lsp

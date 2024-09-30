---
authors:
- "Christoph B\xF6hmwalder"
- Jeremy Grifski
- rzuckerm
date: 2018-08-28
featured-image: hello-world-in-tex.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- tex
title: Hello World in Tex
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/tex/how-to-implement-the-solution.md
- sources/programs/hello-world/tex/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Tex](https://sampleprograms.io/languages/tex) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```tex
%&pdftex

Hello, World!
\end

```

{% endraw %}

Hello World in [Tex](https://sampleprograms.io/languages/tex) was written by:

- Christoph Böhmwalder

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dive right into Hello World in Tex.

It is much simpler in Tex due to the fact the Tex is a markup language.

```tex
%&pdftex
```

This first line is a declaring line used to explain that the desired output of this tex file is a pdf.

```tex
Hello, World!
```

This is the body better known as what will be displayed. You could replace that text with anything to have it show up.

```tex
\end
```

Finally, this is saying the document has ended by declaring (`\`) an `end`.


## How to Run the Solution

There are many options for running Tex files both online and offline. This said my personal favorite option is running it online through [Overleaf][1]. They even cover the other options including themselves on their website [here][2].

[1]: https://www.overleaf.com/
[2]: https://www.overleaf.com/learn

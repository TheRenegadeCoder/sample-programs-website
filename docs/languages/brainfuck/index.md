---
authors:
- Jeremy Grifski
- Ron Zuckerman
date: 2018-08-23
featured-image: programming-languages.jpg
last-modified: 2023-12-22
layout: default
tags:
- brainfuck
title: The Brainfuck Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/brainfuck/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Brainfuck page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- Jeremy Grifski
- Ron Zuckerman

## Description

[Brainfuck][1] is an esoteric programming language created in 1992, and notable for 
its extreme minimalism. As people have implemented more and more ridiculous 
programs with the language, it has become relatively well-known over the years. 
Nowadays some see it as the ultimate coding challenge to create something 
useful in Brainfuck.

At the core of the language is a more-than-compact instruction set, comprising
of a whopping eight instructions. Brainfuck uses a machine model consisting of
an infinite list of one-byte cells, an instruction pointer, and a cell pointer.
The instructions can be used to interact with this environment: `<` and `>`
move the cell pointer, `+` and `-` increment or decrement the value of the cell
at the current pointer, and `[` and `]` denote a loop.

A loop only starts when the value of the current cell is non-zero, otherwise
execution jumps to the end of the loop. Likewise, a loop ends when the value is
zero, otherwise the program jumps to the beginning of the loop. The remaining
two instructions, `,` and `.` read one character from the input into the current
cell and write one character from the current cell to the output, respectively.
That's it!

[1]: https://en.wikipedia.org/wiki/Brainfuck


## Articles

There are 8 articles:

- [Baklava in Brainfuck](https://sampleprograms.io/projects/baklava/brainfuck)
- [Capitalize in Brainfuck](https://sampleprograms.io/projects/capitalize/brainfuck)
- [Fizz Buzz in Brainfuck](https://sampleprograms.io/projects/fizz-buzz/brainfuck)
- [Hello World in Brainfuck](https://sampleprograms.io/projects/hello-world/brainfuck)
- [Longest Word in Brainfuck](https://sampleprograms.io/projects/longest-word/brainfuck)
- [Remove All Whitespace in Brainfuck](https://sampleprograms.io/projects/remove-all-whitespace/brainfuck)
- [Reverse String in Brainfuck](https://sampleprograms.io/projects/reverse-string/brainfuck)
- [Rot13 in Brainfuck](https://sampleprograms.io/projects/rot13/brainfuck)
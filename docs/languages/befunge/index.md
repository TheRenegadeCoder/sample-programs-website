---

title: The Befunge Programming Language
layout: default
last-modified: 2020-05-02
featured-image:
tags: [befunge]
authors:
  - stuin

---

Welcome to the Befunge page! Here, you'll find a description of the language as well as a list of sample programs in that language.

## Description

Befunge is a programming language with some very unusual standards, as a two-dimensional, self-modifying, stack-based programming language. [Wikipedia][2] has it that it was designed in 1993 by Chris Pressey, merely to be as difficult to compile as possible.

All operations in Befunge are limited to a single character, and the source text can be traversed in any direction through the file. The "Instruction Pointer" starts in the upper left corner and proceeds to the right, running every character it crosses. When it reaches an arrow, `< > ^ v`, that pointer will turn and travel in the new indicated direction.

Instead of variables, all operations act on one global stack of integers, similar to [Forth][3]. 0-9 will just push their value, `+ - * / %` pop the top two values and push their normal result, `.` prints out the top number, and `,` prints the corresponding character instead.


## Articles

- [Baklava in Befunge](https://sampleprograms.io/projects/baklava/befunge)
- [Fizz Buzz in Befunge](https://sampleprograms.io/projects/fizz-buzz/befunge)
- [Hello World in Befunge](https://sampleprograms.io/projects/hello-world/befunge)
- [Quine in Befunge](https://sampleprograms.io/projects/quine/befunge)
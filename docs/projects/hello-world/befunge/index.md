---
authors:
- Jeremy Grifski
- rzuckerm
- Stuart
- Stuart Irwin
date: 2018-11-27
featured-image: hello-world-in-befunge.jpg
last-modified: 2023-05-15
layout: default
tags:
- befunge
- hello-world
title: Hello World in Befunge
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/befunge/how-to-implement-the-solution.md
- sources/programs/hello-world/befunge/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Befunge](https://sampleprograms.io/languages/befunge) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```befunge
0"!dlroW ,olleH"v    
                > , v
                | : <
                @    

```

{% endraw %}

Hello World in [Befunge](https://sampleprograms.io/languages/befunge) was written by:

- Stuart Irwin

This article was written by:

- Jeremy Grifski
- rzuckerm
- Stuart
- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

There are many valid ways to set up a Befunge program. People tend to design for either artistic or compactness purposes.

In Befunge, everything works off of a stack. A stack in programming is a list of values, set up sort of like a stack of papers. Only the top number can be retrieved, and new numbers are always placed on the very top. Because of this, strings have to be read in backwards, as the last letter in will be the first letter out.

The program starts out in string mode to read in the characters. At the end of the first line, our stack will look something like this: (with translated characters below)

```
33 100 108 114 111 87 32 44 111 108 108 101 72
!  d   l   r   o   W     ,  o   l   l   e   H
```

The following section is a literal loop, to print out each of the values off the stack:

```befunge
> , v
| : <
@
```

In order, the arrow sends it right, `,` prints out the H, the arrows loop it back around, `:` copies the top value of the stack, and `|` takes that copy for an if statement.

With `|`, if the top value is 0 (or null), then the pointer starts to go downwards, otherwise it is sent up. `_` works the same way, except it means right on 0 and left for anything else.

The pointer will continue to run through the loop until the stack is empty. When it finishes, the if bar drops it down to the bottom. The `@`  indicates end of program. 


## How to Run the Solution

Because of the particular design of the language, your best option is a Befunge interpreter. This is both for availability and because watching it run is the only way to really understand (or debug) it.

- [Befunge Playground][2]
- [jsFunge IDE][3]
- [Befunge-93 Interpreter][4]

There are compilers as well, even through the technical challenges:

- [BefunUtils][6]

For a much more thorough look at Befunge, it's list of operators, and its various derivatives, I recommend the [Esolang Wiki][7].

[2]: https://www.bedroomlan.org/tools/befunge-playground/#prog=hello,mode=edit
[3]: https://befunge.flogisoft.com/
[4]: http://qiao.github.io/javascript-playground/visual-befunge93-interpreter/
[6]: https://github.com/Mikescher/BefunUtils
[7]: https://esolangs.org/wiki/Befunge

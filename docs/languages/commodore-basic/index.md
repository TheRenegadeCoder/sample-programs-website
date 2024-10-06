---
authors:
- rzuckerm
date: 2023-09-13
featured-image: programming-languages.jpg
last-modified: 2024-01-22
layout: default
tags:
- commodore-basic
title: The Commodore Basic Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/commodore-basic/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Commodore Basic page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- rzuckerm

## Description

### Introduction

According to [Wikipedia][1], Commodore BASIC is a dialect of the [BASIC][2]
programming language developed for Commodore's 8-bit home computers. It is
based on [Microsoft BASIC][3], which was developed by Microsoft founders
Bill Gates and Paul Allen. In 1977, Commodore licensed Microsoft BASIC for
a [one-time fee of $25,000][4].

BASIC was the first language I ever learned back in High School. Although I
never owned a Commodore computer, Commodore BASIC is very similar to what I
learned.

### Line Numbers

Like other dialects of BASIC at the time, programs were entered using
[line numbers][5]. The line numbers determine the order of statements in the
program. If an existing line number is used, the code at that line number is
overwritten. If a line number with nothing after it is used, the code at that
line number is deleted. Code can be inserted between existing lines by
using a line number that is between two existing line number. For example,

```basic
10 PRINT "Hello"
20 PRINT "Goodbyte"
15 PRINT "Something else"
20 PRINT "Goodbye"
30 PRINT "All Done"
30
```

This would result in the following code (this can be seen using the [LIST][6]
command, which shows the current program):

```basic
10 PRINT "Hello"
15 PRINT "Something else"
20 PRINT "Goodbye"
```

- Line 10 and 20 are added to the program.
- Line 15 is inserted between lines 10 and 20.
- Line 20 is changed from `PRINT "Goodbyte"` to `PRINT "Goodbye"`.
- Line 30 is added and then deleted.

Line were typically numbered in increments of 10 so that lines could be easily
inserted.

### Statements

Statements are only allowed to be 80 characters long. Multiple statements can
be chained together using `:`. For example, "Hello" and "World" can be
displayed on separate lines like this:

```basic
10 PRINT "Hello": PRINT "World"
```

All keywords are capitalized.

### Variables

There are [three types of variables][7]:

- Real - 32-bit single-precision floating point value ranging from about
  +/-2.9E-38   to +/-1.7E+38. This is the default variable type. It has no
  suffix -- e.g., `N`.
- Integer - 16-bit value ranging from -32768 to 32767. Integer variables are
  denoted with a `%` suffix -- e.g., `A%`.
- String - A sequence of 0 to 255 characters. String variables are denoted
  with a `$` suffix -- e.g., `S$`.

All three types support [arrays][14].

All variables are global. There are some system variables:

- [ST/STATUS][8] - The status of the last file I/O operation
- [TI/TIME][9] - Timer which starts at 0 when the program starts and
  increments every 1/60 of a second.
- [TI$/TIME$][10] - The current time in hours, minutes, and seconds as a
  string -- e.g., `"134725"` corresponds to 13:47:25 in 24-hour time.

Although [variable names][11] can be longer than two characters, only the first
two characters matter -- e.g., `ABC` is the same as `AB`. No part of a
variable name can contain a keyword. For example, `AIF3` is not allowed since
it contains the `IF` keyword.

### Control Flow

Like other BASICs of the time, Commodore BASIC is a completely unstructured
language. Therefore, it uses (gasp!) [GOTO][12] statements to unconditionally
jump to another part of the program.

The [IF][13] statement is used to execute a piece of code conditionally. It
can also be used in conjunction with `GOTO` to jump to another part of the program.
For example:

```basic
50 IF A < 5 THEN B = 7: GOTO 70
60 B = 8
70 PRINT "A ="; A; ", B ="; B
```

If the value of `A` is less than 5, the value of `B` is set to 7, and the code
jumps to line 70. Otherwise, the value of `B` is set to 8. At line 70, the
value of `A` and `B` are displayed.

The [FOR][15] statement can be used to set up loops, where a variable is set
up to go over specified range and increment. For example, this displays the
number 1 to 10:

```basic
100 FOR I = 1 TO 10
110 PRINT I
120 NEXT I
```

The value of `I` runs from 1 to 10. The [NEXT][16] keyword determines the end
of the loop. The [STEP][17] keyword can be used to set the increment for the
loop. For example, this displays even numbers from 10 down to 0:

```basic
100 FOR I = 10 TO 0 STEP -2
110 PRINT I
120 NEXT I
```

Subroutines are supported via the [GOSUB][18] statement. This pushes the line
number of the next instruction to be executed on to the stack and jumps to
the specified line number. The [RETURN][19] statement is used to return
control back to the caller. It pops the line number off the stack and jumps
to that line number. For example:

```basic
150 A = 1: B = 7: GOSUB 1000
160 PRINT "The sum from"; A; "to"; B; "is"; S
170 ...
1000 S = 0
1010 FOR I = A TO B
1020 S = S + I
1030 NEXT I
1040 RETURN
```

At line 150, `A` is set to 1, and `B` is set to 7. Line number 160 is pushed on
to the stack, and the program jumps to line 1000. The code a line 1000 through
1030 sets the value of `S` to the sum of `A` through `B` inclusive. At line
1040, the `RETURN` statement pops 160 from the stack and jumps to that line
number. At line 160 the value of `A`, `B`, and `S` are displayed:

```
The sum from 1 to 7 is 28
```

Finally, the [END][20] statement can be used to stop the execution of the
program. It is typically used in the middle of a program. For the above
example, if line 170 were an `END` statement the program would exit instead
of falling through to line 1000.

### Further Reading

This is just an overview of the Commodore BASIC language. If you want a more
in-depth look at this language, see the [Commodore BASIC Wiki][21]. If you'd
like to try out this language, then clone the [cbmbasic][22] GitHub
repository, change to the directory where the repository was cloned, and run
the `make` command to build the code. For example:

```bash
git clone git@github.com:mist64/cbmbasic.git
cd cbmbasic
make
```

The output will be called `cbmbasic`. If you just run `cbmbasic` with no
arguments, you should see something like this:

```
    **** COMMODORE 64 BASIC V2 ****

 64K RAM SYSTEM  38911 BASIC BYTES FREE

READY.
```

This will take you into the BASIC interpreter where you can enter a program.
You can also run a BASIC program using `cbmbasic` followed by the path to
the program. For example:

```bash
cbmbasic hello-world.bas
```

[1]: https://en.wikipedia.org/wiki/Commodore_BASIC
[2]: https://en.wikipedia.org/wiki/BASIC
[3]: https://en.wikipedia.org/wiki/Microsoft_BASIC
[4]: https://www.c64-wiki.com/wiki/Microsoft#Commodore_BASIC
[5]: https://www.c64-wiki.com/wiki/BASIC#Entering_a_BASIC_program
[6]: https://www.c64-wiki.com/wiki/LIST
[7]: https://www.c64-wiki.com/wiki/Variable#Variables_in_BASIC
[8]: https://www.c64-wiki.com/wiki/STATUS
[9]: https://www.c64-wiki.com/wiki/TIME
[10]: https://www.c64-wiki.com/wiki/TIME$
[11]: https://www.c64-wiki.com/wiki/Variable#Names_of_Variables
[12]: https://www.c64-wiki.com/wiki/GOTO
[13]: https://www.c64-wiki.com/wiki/IF
[14]: https://www.c64-wiki.com/wiki/Array
[15]: https://www.c64-wiki.com/wiki/FOR
[16]: https://www.c64-wiki.com/wiki/NEXT
[17]: https://www.c64-wiki.com/wiki/STEP
[18]: https://www.c64-wiki.com/wiki/GOSUB
[19]: https://www.c64-wiki.com/wiki/RETURN
[20]: https://www.c64-wiki.com/wiki/END
[21]: https://www.c64-wiki.com/wiki/BASIC
[22]: https://github.com/mist64/cbmbasic


## Articles

There are 37 articles:

- [Baklava in Commodore Basic](https://sampleprograms.io/projects/baklava/commodore-basic)
- [Binary Search in Commodore Basic](https://sampleprograms.io/projects/binary-search/commodore-basic)
- [Bubble Sort in Commodore Basic](https://sampleprograms.io/projects/bubble-sort/commodore-basic)
- [Capitalize in Commodore Basic](https://sampleprograms.io/projects/capitalize/commodore-basic)
- [Convex Hull in Commodore Basic](https://sampleprograms.io/projects/convex-hull/commodore-basic)
- [Depth First Search in Commodore Basic](https://sampleprograms.io/projects/depth-first-search/commodore-basic)
- [Dijkstra in Commodore Basic](https://sampleprograms.io/projects/dijkstra/commodore-basic)
- [Duplicate Character Counter in Commodore Basic](https://sampleprograms.io/projects/duplicate-character-counter/commodore-basic)
- [Even Odd in Commodore Basic](https://sampleprograms.io/projects/even-odd/commodore-basic)
- [Factorial in Commodore Basic](https://sampleprograms.io/projects/factorial/commodore-basic)
- [Fibonacci in Commodore Basic](https://sampleprograms.io/projects/fibonacci/commodore-basic)
- [File Input Output in Commodore Basic](https://sampleprograms.io/projects/file-input-output/commodore-basic)
- [Fizz Buzz in Commodore Basic](https://sampleprograms.io/projects/fizz-buzz/commodore-basic)
- [Fraction Math in Commodore Basic](https://sampleprograms.io/projects/fraction-math/commodore-basic)
- [Hello World in Commodore Basic](https://sampleprograms.io/projects/hello-world/commodore-basic)
- [Insertion Sort in Commodore Basic](https://sampleprograms.io/projects/insertion-sort/commodore-basic)
- [Job Sequencing in Commodore Basic](https://sampleprograms.io/projects/job-sequencing/commodore-basic)
- [Josephus Problem in Commodore Basic](https://sampleprograms.io/projects/josephus-problem/commodore-basic)
- [Linear Search in Commodore Basic](https://sampleprograms.io/projects/linear-search/commodore-basic)
- [Longest Common Subsequence in Commodore Basic](https://sampleprograms.io/projects/longest-common-subsequence/commodore-basic)
- [Longest Palindromic Substring in Commodore Basic](https://sampleprograms.io/projects/longest-palindromic-substring/commodore-basic)
- [Longest Word in Commodore Basic](https://sampleprograms.io/projects/longest-word/commodore-basic)
- [Maximum Array Rotation in Commodore Basic](https://sampleprograms.io/projects/maximum-array-rotation/commodore-basic)
- [Maximum Subarray in Commodore Basic](https://sampleprograms.io/projects/maximum-subarray/commodore-basic)
- [Merge Sort in Commodore Basic](https://sampleprograms.io/projects/merge-sort/commodore-basic)
- [Minimum Spanning Tree in Commodore Basic](https://sampleprograms.io/projects/minimum-spanning-tree/commodore-basic)
- [Palindromic Number in Commodore Basic](https://sampleprograms.io/projects/palindromic-number/commodore-basic)
- [Prime Number in Commodore Basic](https://sampleprograms.io/projects/prime-number/commodore-basic)
- [Quick Sort in Commodore Basic](https://sampleprograms.io/projects/quick-sort/commodore-basic)
- [Quine in Commodore Basic](https://sampleprograms.io/projects/quine/commodore-basic)
- [Remove All Whitespace in Commodore Basic](https://sampleprograms.io/projects/remove-all-whitespace/commodore-basic)
- [Reverse String in Commodore Basic](https://sampleprograms.io/projects/reverse-string/commodore-basic)
- [Roman Numeral in Commodore Basic](https://sampleprograms.io/projects/roman-numeral/commodore-basic)
- [Rot13 in Commodore Basic](https://sampleprograms.io/projects/rot13/commodore-basic)
- [Selection Sort in Commodore Basic](https://sampleprograms.io/projects/selection-sort/commodore-basic)
- [Sleep Sort in Commodore Basic](https://sampleprograms.io/projects/sleep-sort/commodore-basic)
- [Transpose Matrix in Commodore Basic](https://sampleprograms.io/projects/transpose-matrix/commodore-basic)
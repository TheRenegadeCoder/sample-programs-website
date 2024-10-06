---
authors:
- rzuckerm
date: 2023-08-23
featured-image: programming-languages.jpg
last-modified: 2023-09-09
layout: default
tags:
- unicat
title: The Unicat Programming Language
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/languages/unicat/description.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the Unicat page! Here, you'll find a description of the language as well as a list of sample programs in that language.

This article was written by:

- rzuckerm

## Description

<style>
.cat {
    font-size: 24px
}
</style>

### Introduction

If you love cats and you love emojis, then you'll *love* this language
since it is entirely composed of cat emojis! But seriously, this is an
[esoteric language][1], so it is designed to be challenging and difficult
to do anything useful.

The Unicat language was created by [gemdude46][2]. Sadly, there was no
documentation that described how to use it. In order to learn this language,
I had to [study the code][3]. It is written in python2, which went
[End-of-Life on January 1, 2020][4]. Fortunately, I had a python2.7
interpreter, so I was able to run the [example programs][5] and put them
on the [python2.7 debugger][6] to figure out parts of the code that I couldn't
figure out by just reading the code.

### Character Set

There are 9 cat emojis that make up the character set for this language. Each
one of these characters represent a byte code from `"0"` to `"8"`:

| Emoji                       | Byte Code | [Emoji type][7]                |
| --------------------------- | --------- | ------------------------------ |
| <span class="cat">😸</span> | `"0"`     | Grinning Cat with Smiling Eyes |
| <span class="cat">😹</span> | `"1"`     | Cat with Tears of Joy          |
| <span class="cat">😺</span> | `"2"`     | Grinning Cat                   |
| <span class="cat">😻</span> | `"3"`     | Smiling Cat with Heart-Eyes    |
| <span class="cat">😼</span> | `"4"`     | Cat with Wry Smile             |
| <span class="cat">😽</span> | `"5"`     | Kissing Cat                    |
| <span class="cat">😾</span> | `"6"`     | Pouting Cat                    |
| <span class="cat">😿</span> | `"7"`     | Crying Cat                     |
| <span class="cat">🙀</span> | `"8"`     | Weary Cat                      |

Anything that is not a cat emoji is ignored, so code comments can be placed
within code without affecting the operation.

### Memory

Memory is made of an arbitrarily large set of addresses that are capable of
storing arbitrarily large values. In other words, it is a python dictionary
where the key is the address and the value is the integer contents of that
address. Any uninitialized memory address is assumed to be zero.

Memory address -1 is a special address that contains the address of the
current instruction to execute. This is initialized to -1 and is incremented
before each instruction is executed.

It should be noted that the instruction memory and the memory that the
program uses are entirely separate, so a program cannot modify itself.

### Numbers

Numbers that are used in instructions are represented in octal (base 8), and
each digit is converted to the corresponding emoji. The number is terminated
with <span class="cat">🙀</span> (`"8"`). If the number is negative, the next
emoji is <span class="cat">😿</span> (`"7"`). Otherwise, it may be terminated
with any other cat emoji. For the sake of brevity, let just use
<span class="cat">🙀</span> (`"8"`) for positive numbers. For example:

| Decimal Value | Octal Value | Emojis                              | Byte Code |
| ------------- | ----------- | ----------------------------------- | --------- |
| 457           | `0o711`     | <span class="cat">😿😹😹🙀🙀</span> | `"71188"` |
| -345          | `-0o531`    | <span class="cat">😽😻😹🙀😿</span> | `"53187"` |

The `0o` is just a common way of represental octal values in several
programming languages like C and Python, to name a few.

Any character needs to be represented by its ASCII (or Unicode) value. For
example, the ASCII value of `"H"` is 72 (`0o110`), so `"H"` is represented as
this:

<span class="cat">😹😹😸🙀🙀</span> (`"11088"`)

One of the oddities of the way numbers are handled is that if there are no
more emojis to process, the number is interpreted as 1337. Why 1337? Well, all
I can figure is that this is actually a [leet code][8] representation for the
word "elite".

### Instructions

Unicat supports these 12 instructions:

| Mnemonic  | Arguments             | Emojis                          | Byte Code    |
| --------- | --------------------- | ------------------------------- | ------------ |
| `asgnlit` | `MEMADDR` `VALUE`     | <span class="cat">😻😹</span>   | `"31"`       |
| `jumpif>` | `MEMADDR` `INSADDR`   | <span class="cat">😽😿</span>   | `"57"`       |
| `echovar` | `MEMADDR`             | <span class="cat">😽😼</span>   | `"54"`       |
| `echoval` | `MEMADDR`             | <span class="cat">😼😼</span>   | `"44"`       |
| `pointer` | `MEMADDR`             | <span class="cat">😼😾</span>   | `"46"`       |
| `randomb` | `MEMADDR`             | <span class="cat">🙀😻</span>   | `"83"`       |
| `inputst` | `MEMADDR`             | <span class="cat">😺😼</span>   | `"24"`       |
| `applop-` | `MEMADDR1` `MEMADDR2` | <span class="cat">😿🙀😺</span> | `"782"`      |
| `applop*` | `MEMADDR1` `MEMADDR2` | <span class="cat">😿🙀🙀</span> | `"788"`      |
| `applop/` | `MEMADDR1` `MEMADDR2` | <span class="cat">😿🙀😿</span> | `"787"`      |
| `applop+` | `MEMADDR1` `MEMADDR2` | <span class="cat">😿🙀😸</span> | `"780"` (\*) |
| `diepgrm` |                       | <span class="cat">🙀🙀</span>   | `"88"`       |

(\*) `applop+` can actually be respresented by any of the following:

* <span class="cat">😿🙀😹</span> (`"781"`)
* <span class="cat">😿🙀😻</span> (`"783"`)
* <span class="cat">😿🙀😼</span> (`"784"`)
* <span class="cat">😿🙀😽</span> (`"785"`)
* <span class="cat">😿🙀😾</span> (`"786"`)

However, let's just stick with what is in the above table.

If an invalid instruction is detected, the program will just jump back to the
beginning, creating an infinite loop. This also happens if there are no more
instructions to process.

The subsequent sections describe each of the instructions and their
corresponding arguments.

#### `asgnlit`

The `asgnlit` instruction stores a value to a memory address. It takes two
arguments:

* `MEMADDR` - The memory address to store the value
* `VALUE` - The value to store

For example, let's set memory address 14 (`0o16`) to -8 (`-0o10`):

<span class="cat">😻😹 😹😾🙀🙀 😹😸🙀😿</span> (`"31 1688 1087"`)

Note that the spaces are just added to delineate the mnemonic from the
arguments.

If `MEMADDR` is -1, the `VALUE` is the instruction address minus 1. This
acts like an unconditional jump to instruction address `VALUE` plus 1.

For example, let's jump to instruction address 22 (`0o26`). Since the
`VALUE` is the instruction address minus 1, this will need to be represented
as 21 (`0o25`):

<span class="cat">😻😹 😹🙀😿 😺😾🙀🙀</span> (`"31 187 2588"`)

#### `jumpif>`

The `jumpif>` instruction compares a value of a memory address to zero. If it
is greater than zero, then the instruction address is changed to the specified
value. Otherwise, the instruction address goes to the next address. This acts
like a conditional jump. It takes two arguments:

* `MEMADDR` - The memory address to compare
* `INSADDR` - The instruction address minus 1

For example, let's jump to instruction address 30 (`0o36`) if the value of
memory address 16 (`0o20`) is greater than 0. The instruction address needs to
be represented as 29 (`0o35`):

<span class="cat">😽😿 😺😸🙀🙀 😻😽🙀🙀</span> (`"57 2088 3588"`)

#### `echovar`

The `echovar` instruction outputs the value of a memory address as
ASCII/Unicode to standard out. It takes a single argument:

* `MEMADDR` - The memory address to output as ASCII/Unicode

For example, let's output the value of memory address 7 (`0o7`):

<span class="cat">😽😼 😿🙀🙀</span> (`"54 788"`)

If memory address contains 117, a `u` is output since 117 is the ASCII code
for `u`.

#### `echoval`

The `echoval` instruction outputs the value of a memory address as digits to
standard out. It takes a single argument:

* `MEMADDR` - The memory address to output as digits

For example, let's output the value of memory address 6 (`0o6`):

<span class="cat">😼😼 😾🙀🙀</span> (`"44 688"`)

If memory address contains 10, a `10` is output.

#### `pointer`

The `pointer` instruction treat a memory address as a pointer to second memory
address and stores the value of that memory address to the first one. It takes
a single argument:

* `MEMADDR` - The memory address to use as a pointer

This is best explained with a diagram:

```
          Before                           After
    ===================              ===================

    | Memory  |       |              | Memory  |       |
    | Address | Value |              | Address | Value |
    +---------+-------+              +---------+-------+
    | 3       | 7     | ---    =>    | 3       | 5     |
    +---------+-------+   |          +---------+-------+ 
--> | 7       | 5     |   |          | 7       | 5     |
|                         |
---------------------------

```

In this diagram, memory address 3 contains a value of 7. The value of memory
address 7 is 5. Therefore, memory address 3 will contain 5, and memory address
7 remains unchanged.

For the above case, the instruction would look like this:

<span class="cat">😼😾 😻🙀🙀</span> (`"46 388"`)

#### `randomb`

The `randomb` instruction sets a memory address to a random boolean value of
0 or 1. It takes a single argument:

* `MEMADDR` - The memory address to store the random boolean value

For example, let's set a random boolean value to address 14 (`0o16`):

<span class="cat">🙀😻 😹😾🙀🙀</span> (`"83 1688"`)

#### `inputst`

The `inputst` instruction reads a line from standard in and stores its
ASCII/Unicode value to a set of memory addresses starting at the specified
memory address. Each ASCII/Unicode value is stored in subsequent memory
addresses. Finally, a 0 value is stored in the next memory address to
null-terminate the line. It takes a single argument:

* `MEMADDR` - The starting memory address to store the input line

For example, let's store the input line to memory address 8 (`0o10`):

<span class="cat">😺😼 😹😸🙀🙀</span> (`"24 1088"`)

If the input line is `"Hello"` followed by a newline (`"\n"`). This is the
result:

* Memory address 8  = `"H"` (72)
* Memory address 9  = `"e"` (101)
* Memory address 10 = `"l"` (108)
* Memory address 11 = `"l"` (108)
* Memory address 12 = `"o"` (111)
* Memory address 13 = `"\n"` (10)
* Memory address 14 = `"\0"` (0)

where `"\0"` is called the NUL character, which is used in other languages
like C to indicate the end of a string value.

#### `applop`

The `applop` instructions take two arguments:

* `MEMADDR1` - The first memory address
* `MEMADDR2` - The second memory address

It performs the following operation depending upon the mnemonic:

| Mnemonic  | Result                                                                                    |
| --------- | ----------------------------------------------------------------------------------------- |
| `applop+` | Value of `MEMADDR1` equals value of `MEMADDR1` plus value of `MEMADDR2`                   |
| `applop-` | Value of `MEMADDR1` equals value of `MEMADDR1` minus value of `MEMADDR2`                  |
| `applop*` | Value of `MEMADDR1` equals value of `MEMADDR1` times value of `MEMADDR2`                  |
| `applop/` | Value of `MEMADDR1` equals quotient of value of `MEMADDR1` divided by value of `MEMADDR2` |

For example, let's set the value of memory address 9 (`0o11`) to 55 and the
value of memory address 7 (`0o7`) is 10:

| Mnemonic  | Emojis                                           | Byte Code       | Result                                         |
| --------  | ------------------------------------------------ | --------------- | ---------------------------------------------- |
| `applop+` | <span class="cat">😿🙀😸 😹😹🙀🙀 😿🙀🙀</span> | `"780 1188 788"` | Memory address 9 value is `55 + 10 = 65`       |
| `applop-` | <span class="cat">😿🙀😸 😹😹🙀🙀 😿🙀🙀</span> | `"782 1188 788"` | Memory address 9 value is `55 - 10 = 45`       |
| `applop-` | <span class="cat">😿🙀🙀 😹😹🙀🙀 😿🙀🙀</span> | `"788 1188 788"` | Memory address 9 value is `55 * 10 = 550`      |
| `applop-` | <span class="cat">😿🙀😿 😹😹🙀🙀 😿🙀🙀</span> | `"787 1188 788"` | Memory address 9 value is `floor(55 / 10) = 5` |

### `diepgrm`

The `diepgrm` instruction exits the program. It has no arguments. The program
*must* contain at least one of these somewhere, or the program will go into an
infinite loop.

### Conclusion

Programming in Unicat is really challenging. It feels more like programming
in machine language without the benefit of an assembler. Instead of
translating instructions into hexadecimal, you have to translate them into cat
emojis, some of which look very similar. If your editor has zoom capability,
I highly recommend using that.

When you run your program, there is a good chance it will lock up. Here are
some of the reasons why (other than the obvious logic error):

* You did not translate the instructions into the right emojis.
* You forgot to terminate a number with the right emojis.
* You forgot to add a `diepgrm` instruction.
* Your jump instructions are not going to the right place.

By the way, I got tired of using python 2 and ported Unicat to python 3. I
also fixed a couple of bugs in the original python 2 implementation. The code
is available on [pypi][9], and the source code is available on [GitHub][10].
It has some limited debugging capability which uses the python debugger to do
the heavy lifting.

In the meantime, happy coding <span class="cat">😸</span>!

[1]: https://en.wikipedia.org/wiki/Esoteric_programming_language
[2]: https://github.com/gemdude46/unicat
[3]: https://github.com/gemdude46/unicat/blob/master/cat.py
[4]: https://www.python.org/doc/sunset-python-2/
[5]: https://github.com/gemdude46/unicat/tree/master/examples
[6]: https://docs.python.org/2.7/library/pdb.html
[7]: https://emojipedia.org/cat-face
[8]: https://en.wikipedia.org/wiki/Leet
[9]: https://pypi.org/project/unicat-esolang/
[10]: https://github.com/rzuckerm/unicat-esolang


## Articles

There are 4 articles:

- [Baklava in Unicat](https://sampleprograms.io/projects/baklava/unicat)
- [Fizz Buzz in Unicat](https://sampleprograms.io/projects/fizz-buzz/unicat)
- [Hello World in Unicat](https://sampleprograms.io/projects/hello-world/unicat)
- [Reverse String in Unicat](https://sampleprograms.io/projects/reverse-string/unicat)
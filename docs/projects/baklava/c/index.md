---
authors:
- Jeremy Grifski
- rzuckerm
- Stuart Irwin
- Ștefan-Iulian Alecu
date: 2018-09-17
featured-image: baklava-in-c.jpg
last-modified: 2026-05-15
layout: default
tags:
- baklava
- c
title: Baklava in C
title1: Baklava
title2: in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c/how-to-implement-the-solution.md
- sources/programs/baklava/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C](https://sampleprograms.io/languages/c)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include "stdio.h"

int main(void)
{

    for (int i = 0; i < 10; i++)
    {
        printf("%.*s", (10 - i), "                                 ");
        printf("%.*s", (i * 2 + 1), "******************************");
        printf("\n");
    }

    for (int i = 10; -1 < i; i--)
    {
        printf("%.*s", (10 - i), "                                 ");
        printf("%.*s", (i * 2 + 1), "******************************");
        printf("\n");
    }

    return 0;
}

```

{% endraw %}

Baklava in [C](https://sampleprograms.io/languages/c) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

This article was written by:

- Jeremy Grifski
- rzuckerm
- Stuart Irwin
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

### Header file

```c
#include "stdio.h"
```

This line includes the standard input/output library.

The program uses `printf()` from this library to display text on the screen.
Without including `stdio.h`, the compiler would not know what `printf()` is.

### Main function

```c
int main(void)
```

Every C program begins execution in `main`.

`int` means the function returns an integer value. `void` means the function
takes no arguments. Returning 0 at the end tells the operating system the
program finished successfully.

Everything inside the braces of `main` is executed in order.

### Top half of diamond

```c
for (int i = 0; i < 10; i++)
```

This loop generates the expanding upper half of the diamond.

#### Anatomy of the loop

A `for` loop has this structure:

```c
for (initialization; condition; update)
```

In this program,
```c
int i = 0;
```
creates the loop variable `i` and starts it at 0. Then,
```c
i < 10
```
is checked every iteration. As long as this condition is true, the loop keeps
running.
```c
i++
```
runs after each iteration and increases `i` by one.

As such, `i` ranges from `0` to `9`, giving us ten rows.

#### Printing the leading spaces

```c
printf ("%.*s", (10 - i), "                                 ");
```

This prints the padding before the stars. 

Normally, we use `%s` to print an entire string. But `%.*s` lets us specify the
maximum number of characters to print. As such, `(10 - i)` is passed as that
maximum width.

At the beginning, `i` is 0, so ten spaces are printed. As the number of spaces
decreases, the stars move toward the center.

#### Printing the stars

```c
printf("%.*s", (i * 2 + 1), "******************************");
```

This prints the visible stars, using the same mechanism as above. We use `i *
2 + 1` because every row adds two more stars than before, making the diamond
expand evenly.

#### Moving to the next line

```c
printf("\n");
```

`\n` is the new line character. Without this, all output would appear on the
same line.

### Bottom half of diamond

```c
for (int i = 10; -1 < i; i--)
```

This loop creates the shrinking lower half.

The logic is almost identical to the first loop, except now `i` decreases by one
due to `i--`. The number of spaces increases while the number of stars
decreases, producing the lower half of the diamond.

### Program termination

```c
return 0;
```

This ends the program and returns control to the operating system. A return
value of `0` conventionally means the program executed successfully.


## How to Run the Solution

If we want to compile and run the program on a computer, we first need a C
compiler installed. Common choices include GCC, Clang, and Microsoft Visual
C++ (MSVC).

Once a compiler is available, we can open a terminal in the same directory as
the source file and compile the program.

For example, using GCC:
```sh
gcc -o baklava baklava.c
./baklava
```
or using Clang:
```sh
clang -o baklava baklava.c
./baklava
```
On Windows with the Microsoft compiler:
```sh
cl baklava.c
baklava.exe
```
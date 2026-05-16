---
authors:
- Jeremy Grifski
- shubhragupta-code
- Softizo
- Ștefan-Iulian Alecu
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-15
layout: default
tags:
- c
- capitalize
title: Capitalize in C
title1: Capitalize
title2: in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/c/how-to-implement-the-solution.md
- sources/programs/capitalize/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char *captialize(char str[])
{
    for (int i = 0; i < strlen(str); i++)
        if (i == 0)
            str[i] = toupper(str[i]);
        else
            continue;
    return str;
}

int main(int argc, char *argv[])
{
    if (argc == 2 && strlen(argv[1]) != 0)
        printf("%s\n", captialize(argv[1]));
    else if (argc > 2)
        printf("Use quotes around multiple strings.\n");
    else
        printf("Usage: please provide a string\n");

    return 0;
}

```

{% endraw %}

Capitalize in [C](https://sampleprograms.io/languages/c) was written by:

- Jeremy Grifski
- Softizo
- Ștefan-Iulian Alecu

This article was written by:

- Jeremy Grifski
- shubhragupta-code
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution


### Header files

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>
```

These lines import standard libraries so we can use built-in functions. 

- `<ctype.h>` provides character functions like [`toupper()`][2].
- `<stdio.h>` provides input/output functions like [`printf()`][3].
- `<string.h>` provides string utilities like [`strlen()`][1].

### Main function

```c
int main(int argc, char *argv[])
```

This is where every C program starts. Here, `argc` represents the number of
command-line arguments, and `argv` represents an array of strings containing
those arguments. So, if we run:

```console
./capitalize "hello"
```
then:
- `argc = 2`
- `argv[0] = "./capitalize"`
- `argv[1] = "hello"`

### Input validation

```c
if (argc == 2 && strlen(argv[1]) != 0)
```

This ensures:

- exactly one argument is provided
- it is not an empty string

If the user provides no input, the program prints usage message. If there are
too many arguments, the program warns about quotes, because the user most
likely called the program using `./capitalize hello world` instead of
`./capitalize "hello world"`.

### Capitalization step

```c
printf("%s\n", capitalize(argv[1]));
```

If input is valid, we call `capitalize()` with the first argument, then print
the result. In the function:

```c
char *captialize(char str[])
{
    for (int i = 0; i < strlen(str); i++)
        if (i == 0)
            str[i] = toupper(str[i]);
        else
            continue;
    return str;
}
```
we traverse each letter in the string. If `i = 0`, then we capitalize the first
letter of the string using [`toupper`][2], otherwise the string remains the same.

[1]: https://man7.org/linux/man-pages/man3/strlen.3.html
[2]: https://man7.org/linux/man-pages/man3/toupper.3.html
[3]: https://man7.org/linux/man-pages/man3/printf.3.html

## How to Run the Solution

If we want to compile and run the program on a computer, we first need a C
compiler installed. Common choices include GCC, Clang, and Microsoft Visual
C++ (MSVC).

Once a compiler is available, we can open a terminal in the same directory as
the source file and compile the program.

For example, using GCC:
```sh
gcc -o capitalize capitalize.c
./capitalize
```
or using Clang:
```sh
clang -o capitalize capitalize.c
./capitalize
```
On Windows with the Microsoft compiler:
```sh
cl capitalize.c
capitalize.exe
```
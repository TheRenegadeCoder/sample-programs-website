---
authors:
- Abhishek Dinkar Raut
- "Christoph B\xF6hmwalder"
- Jeremy Grifski
- rzuckerm
date: 2018-07-24
featured-image: reverse-string-in-c.jpg
last-modified: 2023-05-15
layout: default
tags:
- c
- reverse-string
title: Reverse String in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/c/how-to-implement-the-solution.md
- sources/programs/reverse-string/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    char *text = "";
    size_t textlen;

    /* get text from command line and calculate length */
    if (argc >= 2) {
        text = argv[1];
    }

    textlen = strlen(text);

    /* print characters in reverse */
    while (textlen-- > 0) {
        putchar(text[textlen]);
    }

    /* put a newline at the end */
    putchar('\n');

    return 0;
}

```

{% endraw %}

Reverse String in [C](https://sampleprograms.io/languages/c) was written by:

- Christoph Böhmwalder
- rzuckerm

This article was written by:

- Abhishek Dinkar Raut
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

### Approach

We get the length of the input string and iteration from the last character to the first, displaying each character.

[Time complexity][1]: O(n)

<br/>

### Breakdown

Now let us see step-by-step how the code works.

```c
#include <stdio.h> 
#include <string.h> 
```

Here we are including header files (`.h` files) to use functions like `printf()`. Header files provided us with tested ready to use functions to ease the software development work. 

By including `#include <stdio.h>` we can use `printf()` method without worrying about how it is implemented.

```c
int main(int argc, char **argv)
{
    char *text = "";
    size_t textlen;

    /* get text from command line and calculate length */
    if (argc >= 2) {
        text = argv[1];
    }

    textlen = strlen(text);
```

This get the first command-line argument if it is present. Otherwise, an empty string it assumed. The variable `text` contains
a pointer to the string to be reversed. Then, the length of the string is calculated using **strlen()** and stored in `textlen`.

Now we get to actual code that displays the string in reverse:

```c
/* print characters in reverse */
while (textlen-- > 0) {
    putchar(text[textlen]);
}
```

This goes through the string in reverse order and displays each character.

Then, a newline is displayed:

```c
/* put a newline at the end */
putchar('\n');
```

Finally the code exits:

```c
return 0;
```

[1]: https://en.wikipedia.org/wiki/Time_complexity


## How to Run the Solution

The easiest way to run this program is to go to this [LeetCode Playground][2] and run the program. You can tweak the program or provide different input strings to understand how it works.

Alternatively, you can copy the [code from GitHub][3] code and run the program on an [online C compiler][4] or in an IDE.

[2]: https://leetcode.com/
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/c/c/reverse-string.c
[4]: https://www.onlinegdb.com/online_c_compiler

---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-11
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-15
layout: default
tags:
- c
- zeckendorf
title: Zeckendorf in C
title1: Zeckendorf
title2: in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/c/how-to-implement-the-solution.md
- sources/programs/zeckendorf/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <errno.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static void usage(void)
{
    fputs("Usage: please input a non-negative integer\n", stderr);
    exit(EXIT_FAILURE);
}

void zeckendorf(uint64_t n)
{
    if (n == 0)
    {
        putchar('\n');
        return;
    }

    uint64_t a = 1, b = 2;

    while (b <= n)
    {
        uint64_t next = a + b;
        a = b;
        b = next;
    }

    bool first = true;

    while (n > 0)
    {
        if (a <= n)
        {
            if (!first)
                fputs(", ", stdout);
            printf("%" PRIu64, a);
            n -= a;
            first = false;
        }

        uint64_t prev = b - a;
        b = a;
        a = prev;
    }

    putchar('\n');
}

int main(int argc, char *argv[])
{
    if (argc != 2)
        usage();

    const char *s = argv[1];
    char *end = NULL;

    errno = 0;
    uint64_t n = strtoull(s, &end, 10);

    if (*s == '\0' || *end != '\0' || errno == ERANGE || *s == '-')
        usage();

    zeckendorf(n);
    return EXIT_SUCCESS;
}
```

{% endraw %}

Zeckendorf in [C](https://sampleprograms.io/languages/c) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- "Christoph B\xF6hmwalder"
- Jeremy Grifski
- Parker Johansen
date: 2018-10-04
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-18
layout: default
tags:
- c
- fibonacci
title: Fibonacci in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/c/how-to-implement-the-solution.md
- sources/programs/fibonacci/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <errno.h>
#include <inttypes.h>
#include <string.h>

/*
 * This limit is chosen because fib(93) is the first number that is
 * still small enough to fit into a 64 bit integer.
 */
#define LIMIT 93

void fibonacci(int n)
{
    unsigned long long first = 0;
    unsigned long long second = 1;
    unsigned long long result = 0;

    for (int i = 1; i <= n; i++) {
        result = first + second;
        first = second;
        second = result;
        printf("%d: %llu\n", i, first);
    }
}

int main(int argc, char **argv)
{
    uintmax_t n;

    if (argc < 2 || strcmp(argv[1], "") == 0) {
        fprintf(stderr, "Usage: please input the count of fibonacci numbers to output\n");
        return 1;
    }

    errno = 0;
    n = strtoumax(argv[1], NULL, 10);
    if (n == 0 && strcmp(argv[1], "0") != 0 || (n == UINTMAX_MAX && errno == ERANGE)) {
        fprintf(stderr, "Usage: please input the count of fibonacci numbers to output\n");
        return 1;
    }

    if (n > LIMIT) {
        fprintf(stderr, "n cannot be larger than %d\n", LIMIT);
        return 1;
    }

    fibonacci(n);
    return 0;
}

```

{% endraw %}

Fibonacci in [C](https://sampleprograms.io/languages/c) was written by:

- Christoph Böhmwalder
- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
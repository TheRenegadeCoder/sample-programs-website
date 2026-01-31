---
authors:
- rzuckerm
date: 2026-01-31
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-01-31
layout: default
tags:
- awk
- zeckendorf
title: Zeckendorf in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/awk/how-to-implement-the-solution.md
- sources/programs/zeckendorf/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please input a non-negative integer"
    exit(1)
}

function str_to_number(s) {
    return (s ~ /^\s*[+-]*[0-9]+\s*$/) ? s + 0 : "ERROR"
}

function fibonacci_up_to(n, fibs,  a, b, c, k) {
    a = 1
    b = 2
    for (k = 1; a <= n; k++) {
        fibs[k] = a
        c = a + b
        a = b
        b = c
    }
}

function zeckendorf(n, zecks,  i, k) {
    fibonacci_up_to(n, fibs)
    k = length(fibs)
    i = 1
    while (k > 0 && n > 0) {
        fib = fibs[k]
        if (fib <= n) {
            zecks[i++] = fib
            n -= fib
            k -= 2
        } else {
            k--
        }
    }
}

function show_array(arr,  idx, s) {
    s = ""
    for (idx in arr) {
        if (s) {
            s = s ", "
        }
        s = s arr[idx]
    }

    print s
}

BEGIN {
    if (ARGC < 2) {
        usage()
    }

    n = str_to_number(ARGV[1])
    if (n == "ERROR" || n < 0) {
        usage()
    }

    zeckendorf(n, zecks)
    show_array(zecks)
}

```

{% endraw %}

Zeckendorf in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
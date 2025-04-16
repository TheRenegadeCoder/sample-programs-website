---
authors:
- rzuckerm
date: 2025-04-14
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- josephus-problem
title: Josephus Problem in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/awk/how-to-implement-the-solution.md
- sources/programs/josephus-problem/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please input the total number of people and number of people to skip."
    exit(1)
}

function str_to_number(s) {
    return (s ~ /^\s*[+-]*[0-9]+\s*$/) ? s + 0 : "ERROR"
}

# Reference: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
#
# Use zero-based index algorithm:
#
#     g(1, k) = 0
#     g(m, k) = [g(m - 1, k) + k] MOD m, for m = 2, 3, ..., n
#
# Final answer is g(n, k) + 1 to get back to one-based index
function josephus_problem(n, k,  g, m) {
    g = 0
    for (m = 2; m <= n; m++) {
        g = (g + k) % m
    }

    return g + 1
}

BEGIN {
    if (ARGC < 3) {
        usage()
    }

    n = str_to_number(ARGV[1])
    k = str_to_number(ARGV[2])
    if (n == "ERROR" || k == "ERROR") {
        usage()
    }

    print josephus_problem(n, k)
}

```

{% endraw %}

Josephus Problem in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2025-04-07
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-04-07
layout: default
tags:
- awk
- prime-number
title: Prime Number in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/awk/how-to-implement-the-solution.md
- sources/programs/prime-number/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

function is_prime(n) {
    result = (n == 2) || (n > 2 && n % 2 != 0)
    q = sqrt(n)
    for (i = 3; result && i <= q; i += 2) {
        result = (n % i != 0)
    }

    return result
}

BEGIN {
    if (ARGC < 2) {
        usage()
    }

    result = str_to_number(ARGV[1])
    if (result == "ERROR" || result < 0) {
        usage()
    }

    print is_prime(result) ? "prime" : "composite"
}

```

{% endraw %}

Prime Number in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
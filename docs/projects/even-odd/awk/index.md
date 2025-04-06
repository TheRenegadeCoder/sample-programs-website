---
authors:
- rzuckerm
date: 2025-04-06
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-04-06
layout: default
tags:
- awk
- even-odd
title: Even Odd in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/awk/how-to-implement-the-solution.md
- sources/programs/even-odd/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please input a number"
    exit(1)
}

function str_to_number(s) {
    return (s ~ /^\s*[+-]*[0-9]+\s*$/) ? s + 0 : "ERROR"
}

function is_even(n) {
    return (n % 2) == 0
}

BEGIN {
    if (ARGC < 2) {
        usage()
    }

    result = str_to_number(ARGV[1])
    if (result == "ERROR") {
        usage()
    }

    print is_even(result) ? "Even" : "Odd"
}

```

{% endraw %}

Even Odd in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2025-04-07
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- palindromic-number
title: Palindromic Number in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/awk/how-to-implement-the-solution.md
- sources/programs/palindromic-number/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

function is_palindromic_number(n,  s, left, right, result) {
    result = 1
    s  = sprintf("%s", n)
    for (left = 1, right = length(s); result && left < right; left++, right--) {
        result = (substr(s, left, 1) == substr(s, right, 1))
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

    print is_palindromic_number(result) ? "true" : "false"
}

```

{% endraw %}

Palindromic Number in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
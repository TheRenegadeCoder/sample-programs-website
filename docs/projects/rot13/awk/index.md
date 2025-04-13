---
authors:
- rzuckerm
date: 2025-04-07
featured-image: rot13-in-every-language.jpg
last-modified: 2025-04-07
layout: default
tags:
- awk
- rot13
title: Rot13 in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/awk/how-to-implement-the-solution.md
- sources/programs/rot13/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string to encrypt"
    exit(1)
}

function rot13(s) {
    input_table  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    output_table = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    result = ""
    for (i = 1; i <= length(s); i++) {
        c = substr(s, i, 1)
        idx = index(input_table, c)
        if (idx > 0) {
            c = substr(output_table, idx, 1)
        }

        result = result c
    }

    return result
}

BEGIN {
    if (ARGC < 2 || !ARGV[1]) {
        usage()
    }

    print rot13(ARGV[1])
}

```

{% endraw %}

Rot13 in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
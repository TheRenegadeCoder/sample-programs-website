---
authors:
- rzuckerm
date: 2025-04-14
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- longest-word
title: Longest Word in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/awk/how-to-implement-the-solution.md
- sources/programs/longest-word/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string"
    exit(1)
}

function longest_word(s,  len, max_len, k) {
    split(s, arr, /\s+/)
    max_len = 0
    for (k in arr) {
        len = length(arr[k])
        if (len > max_len) {
            max_len = len
        }
    }

    return max_len
}

BEGIN {
    if (ARGC < 2 || !ARGV[1]) {
        usage()
    }

    print longest_word(ARGV[1])
}

```

{% endraw %}

Longest Word in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
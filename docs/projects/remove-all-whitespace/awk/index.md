---
authors:
- rzuckerm
date: 2025-04-14
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- remove-all-whitespace
title: Remove All Whitespace in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/awk/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string"
    exit(1)
}

function remove_whitespace(s,  arr, result) {
    split(s, arr, /\s+/)
    result = ""
    for (k in arr) {
        result = result arr[k]
    }

    return result
}

BEGIN {
    if (ARGC < 2 || !ARGV[1]) {
        usage()
    }

    print remove_whitespace(ARGV[1])
}

```

{% endraw %}

Remove All Whitespace in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
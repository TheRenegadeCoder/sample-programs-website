---
authors:
- rzuckerm
date: 2025-04-07
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- reverse-string
title: Reverse String in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/awk/how-to-implement-the-solution.md
- sources/programs/reverse-string/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function reverse_string(s,  result, i) {
    result = ""
    for (i = length(s); i > 0; i--) {
        result = result substr(s, i, 1)
    }

    return result
}

BEGIN {
    if (ARGC > 1) {
        print reverse_string(ARGV[1])
    }
}

```

{% endraw %}

Reverse String in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
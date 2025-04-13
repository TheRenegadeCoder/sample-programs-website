---
authors:
- rzuckerm
date: 2025-04-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-04-06
layout: default
tags:
- awk
- baklava
title: Baklava in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/awk/how-to-implement-the-solution.md
- sources/programs/baklava/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function repeat_string(n, s) {
    result = ""
    for (k = 1; k <= n; k++) {
        result = result s
    }

    return result
}

BEGIN {
    for (i = -10; i <= 10; i++) {
        num_spaces = (i >= 0) ? i : -i
        num_stars = 21 - 2 * num_spaces
        print repeat_string(num_spaces, " ") repeat_string(num_stars, "*")
    }
}

```

{% endraw %}

Baklava in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
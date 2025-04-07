---
authors:
- rzuckerm
date: 2025-04-07
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-04-07
layout: default
tags:
- awk
- fizz-buzz
title: Fizz Buzz in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/awk/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
BEGIN {
    for (i = 1; i <= 100; i++) {
        result = ""
        if (i % 3 == 0) {
            result = result "Fizz"
        }

        if (i % 5 == 0) {
            result = result "Buzz"
        }

        if (!result) {
            result = result sprintf("%d", i)
        }

        print result
    }
}

```

{% endraw %}

Fizz Buzz in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
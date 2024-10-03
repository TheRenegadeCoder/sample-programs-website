---
authors:
- rzuckerm
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- baklava
- rexx
title: Baklava in Rexx
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/rexx/how-to-implement-the-solution.md
- sources/programs/baklava/rexx/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Rexx](https://sampleprograms.io/languages/rexx) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rexx
do i = -10 to 10
    numSpaces = abs(i)
    say strRepeat(numSpaces, " ") || strRepeat(21 - 2 * numSpaces, "*")
end

strRepeat:
    arg n, s
    result = ""
    do while n > 0
        result = result || s
        n = n - 1
    end

    return result

```

{% endraw %}

Baklava in [Rexx](https://sampleprograms.io/languages/rexx) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2024-12-31
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-31
layout: default
tags:
- baklava
- kitten
title: Baklava in Kitten
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/kitten/how-to-implement-the-solution.md
- sources/programs/baklava/kitten/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Kitten](https://sampleprograms.io/languages/kitten) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kitten
define repeat_string (List<Char>, Int32 -> List<Char>):
    -> s, n;
    if (n > 0) {
        s s n 1 (-) repeat_string (+)
    } else {
        ""
    }

define baklava_line (Int32 -> List<Char>):
    -> n;
    n abs -> num_spaces;
    21 2 num_spaces (*) (-) -> num_stars;
    " " num_spaces repeat_string
    "*" num_stars repeat_string (+)

define baklava (Int32, Int32 -> +IO):
    -> n, ne;
    if (n <= ne) {
        n baklava_line say
        n 1 (+) ne baklava
    }

-10 10 baklava

```

{% endraw %}

Baklava in [Kitten](https://sampleprograms.io/languages/kitten) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
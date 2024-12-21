---
authors:
- rzuckerm
date: 2024-12-21
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-21
layout: default
tags:
- baklava
- spry
title: Baklava in Spry
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/spry/how-to-implement-the-solution.md
- sources/programs/baklava/spry/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Spry](https://sampleprograms.io/languages/spry) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```spry
abs = func [:x
    ($x >= 0) then: [ $x ] else: [ 0 - $x ]
]

repeat_string:times: = func [:s :n
    ($n > 0) then: [ $s, repeat_string: $s times: ($n - 1) ] else: [ "" ]
]

-10 to: 10 do: [
    num_spaces = abs :i
    num_stars = (21 - (num_spaces * 2))
    echo (repeat_string: " " times: num_spaces, repeat_string: "*" times: num_stars)
]

```

{% endraw %}

Baklava in [Spry](https://sampleprograms.io/languages/spry) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
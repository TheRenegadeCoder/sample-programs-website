---
authors:
- rzuckerm
date: 2025-01-14
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-14
layout: default
tags:
- baklava
- dusk
title: Baklava in Dusk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/dusk/how-to-implement-the-solution.md
- sources/programs/baklava/dusk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Dusk](https://sampleprograms.io/languages/dusk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dusk
let repeat_string = |s, n| join(alloc(n, s), '')

let n = -10
while n < 11 {
    let num_spaces = n
    if num_spaces < 0: num_spaces = -num_spaces
    let num_stars = 21 - 2 * num_spaces
    n += 1
    println(repeat_string(' ', num_spaces) + repeat_string('*', num_stars))
}

```

{% endraw %}

Baklava in [Dusk](https://sampleprograms.io/languages/dusk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
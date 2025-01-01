---
authors:
- rzuckerm
date: 2024-12-31
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-31
layout: default
tags:
- baklava
- koka
title: Baklava in Koka
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/koka/how-to-implement-the-solution.md
- sources/programs/baklava/koka/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Koka](https://sampleprograms.io/languages/koka) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```koka
fun repeat_string(s : string, n : int) {
    var result := ""
    list(1, n).foreach(fn(_) { result := result + s })
    result
}

fun main() {
    list(-10, 10).foreach(fn(n) {
        var num_spaces := abs(n)
        var num_stars := 21 - 2 * num_spaces
        println(repeat_string(" ", num_spaces) + repeat_string("*", num_stars))
    })
}

```

{% endraw %}

Baklava in [Koka](https://sampleprograms.io/languages/koka) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
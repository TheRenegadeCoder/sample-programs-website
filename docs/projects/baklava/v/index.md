---
authors:
- rzuckerm
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- baklava
- v
title: Baklava in V
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/v/how-to-implement-the-solution.md
- sources/programs/baklava/v/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [V](https://sampleprograms.io/languages/v) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```v
module main

fn str_repeat(n int, s string) string {
    mut result := ""
    for _ in 0 .. n {
        result += s
    }

    return result
}

fn main() {
    for i in -10 .. 11 {
        num_spaces := if i >= 0 { i } else { -i }
        println(str_repeat(num_spaces, " ") + str_repeat(21 - 2 *num_spaces, "*"))
    }
}

```

{% endraw %}

Baklava in [V](https://sampleprograms.io/languages/v) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
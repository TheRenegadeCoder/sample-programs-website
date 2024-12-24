---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- never
title: Baklava in Never
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/never/how-to-implement-the-solution.md
- sources/programs/baklava/never/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Never](https://sampleprograms.io/languages/never) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```never
func abs(n: int) -> int {
    (n < 0) ? -n : n
}

func repeat_string(s: string, n: int) -> string {
    var result = "";
    var i = 0;
    for (i = 0; i < n; i = i + 1) {
        result = result + s
    };

    result
}

func main() -> int {
    var i = 0;
    for (i = -10; i <= 10; i = i + 1) {
        var num_spaces = abs(i);
        var num_stars = 21 - 2 * num_spaces;
        prints(repeat_string(" ", num_spaces) + repeat_string("*", num_stars) + "\n")
    };

    0
}

```

{% endraw %}

Baklava in [Never](https://sampleprograms.io/languages/never) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
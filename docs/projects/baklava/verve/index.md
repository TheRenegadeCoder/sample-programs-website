---
authors:
- rzuckerm
date: 2023-12-21
featured-image: baklava-in-every-language.jpg
last-modified: 2023-12-21
layout: default
tags:
- baklava
- verve
title: Baklava in Verve
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/verve/how-to-implement-the-solution.md
- sources/programs/baklava/verve/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Verve](https://sampleprograms.io/languages/verve) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```verve
fn abs(n: Int) -> Int {
    if (n < 0) { -n } else { n }
}

let baklava_str = "          *********************"

fn baklava_line(n: Int) -> String {
    let num_spaces = abs(n)
    let num_stars = 21 - 2 * num_spaces
    substr(baklava_str, 10 - num_spaces, num_spaces + num_stars)
}

fn baklava(start: Int, end: Int) {
    if not(start > end) {
        print(baklava_line(start))
        baklava(start + 1, end)
    }
}

baklava(-10, 10)

```

{% endraw %}

Baklava in [Verve](https://sampleprograms.io/languages/verve) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
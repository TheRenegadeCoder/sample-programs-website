---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- odin
title: Baklava in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/odin/how-to-implement-the-solution.md
- sources/programs/baklava/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main;

import "core:fmt"
import "core:strings"

main :: proc() {
    for i := -10; i <= 10; i += 1 {
        num_spaces := abs(i)
        num_stars := 21 - 2 * num_spaces
        spaces, _ := strings.repeat(" ", num_spaces)
        stars, _ := strings.repeat("*", num_stars)
        fmt.println(strings.concatenate({spaces, stars}))
    }
}

```

{% endraw %}

Baklava in [Odin](https://sampleprograms.io/languages/odin) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- nallovint
date: 2024-07-12
featured-image: even-odd-in-every-language.jpg
last-modified: 2024-07-12
layout: default
tags:
- even-odd
- odin
title: Even Odd in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/odin/how-to-implement-the-solution.md
- sources/programs/even-odd/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main

import "core:fmt"
import "core:strconv"
import "core:os"

main :: proc() {
    if len(os.args) != 2 {
        usage()
        return
    }
    n, ok := strconv.parse_int(os.args[1])
    if !ok {
        usage()
        return
    }
    evenodd(n)
}

evenodd :: proc(n: int) {
    if n % 2 == 0 {
        fmt.println("Even")
    } else {
        fmt.println("Odd")
    }
}

usage :: proc() {
    fmt.println("Usage: please input a number")
}
```

{% endraw %}

Even Odd in [Odin](https://sampleprograms.io/languages/odin) was written by:

- nallovint

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
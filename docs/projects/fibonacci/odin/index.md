---
authors:
- Omnissiah
date: 2025-10-30
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- fibonacci
- odin
title: Fibonacci in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/odin/how-to-implement-the-solution.md
- sources/programs/fibonacci/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
    input, check := strconv.parse_int(os.args[1], 10)
    if !check {
        usage()
        return
    }

    use1 := 0
    use2 := 1
    use3 := 0
    for i:=1 ; i <= input; i += 1 {
        use3 = use1 + use2
        use1 = use2
        use2 = use3
        fmt.print(i)
        fmt.print(": ")
        fmt.println(use1)
    }
}

usage :: proc() { 
    fmt.println("Usage: please input the count of fibonacci numbers to output")
}

```

{% endraw %}

Fibonacci in [Odin](https://sampleprograms.io/languages/odin) was written by:

- Omnissiah

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
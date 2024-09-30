---
authors:
- nallovint
date: 2024-07-25
featured-image: reverse-string-in-every-language.jpg
last-modified: 2024-07-25
layout: default
tags:
- odin
- reverse-string
title: Reverse String in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/odin/how-to-implement-the-solution.md
- sources/programs/reverse-string/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main

import "core:fmt"
import "core:strings"
import "core:os"

reverse_string :: proc(str : string) {
    sb := strings.builder_make(0, len(str))
    #reverse for ch in str {
        strings.write_rune(&sb, ch)
    }
    fmt.println(strings.to_string(sb))
}

main :: proc() {
    if len(os.args) < 2 {
        return
    }
    reverse_string(os.args[1])
}

```

{% endraw %}

Reverse String in [Odin](https://sampleprograms.io/languages/odin) was written by:

- nallovint

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
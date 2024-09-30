---
authors:
- nallovint
date: 2024-08-03
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-08-03
layout: default
tags:
- longest-word
- odin
title: Longest Word in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/odin/how-to-implement-the-solution.md
- sources/programs/longest-word/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main

import "core:fmt"
import "core:strings"
import "core:os"

main :: proc() {
    if len(os.args) != 2 {
        usage()
        return
    }
    text := os.args[1]
    get_longest_word(text)
}

get_longest_word :: proc (words: string) -> int {
    if len(words) == 0 {
        usage()
        return 0
    }

    cleaned, _ := strings.replace_all(words, "\t", " ")
    cleaned, _ = strings.replace_all(cleaned, "\r", " ")
    cleaned, _ = strings.replace_all(cleaned, "\n", " ")
    string_split := strings.split(cleaned, " ")

    count := 0
    for word in string_split {
        if len(word) > count {
            count = len(word)
        }
    }
    fmt.println(count)
    return count
}

usage :: proc() {
    fmt.eprintln("Usage: please provide a string")
}

```

{% endraw %}

Longest Word in [Odin](https://sampleprograms.io/languages/odin) was written by:

- nallovint

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
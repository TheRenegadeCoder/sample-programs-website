---
authors:
- rzuckerm
date: 2025-01-25
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-25
layout: default
tags:
- baklava
- mirth
title: Baklava in Mirth
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/mirth/how-to-implement-the-solution.md
- sources/programs/baklava/mirth/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Mirth](https://sampleprograms.io/languages/mirth) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mirth
module sample-programs.baklava

import std.prelude
import std.world
import std.list
import std.str

||| stack: n
def abs [Int -- Nat] {
    ||| if n < 0 then -n else n
    dup 0 < if(-1 *, dup drop) Int.>Nat-clamp
}

||| stack: n (count), s (string)
def repeat-string [Nat Str -- Str] {
    ""                      ||| stack: n, s, result = ""
    rotl                    ||| stack: s, result, n
    repeat(                 ||| stack: s, result
                            ||| repeat n times:
        over                |||     stack: s, result, s
        cat                 |||     stack: s, result = result + s
    )
    dip(drop)               ||| stack: result
}

||| stack: n
def baklava-line [Int -- Str] {
    abs                                 ||| stack: num-spaces = abs(n)
    dup                                 ||| stack: num-spaces, num-spaces
    " " repeat-string                   ||| stack: num-spaces, spaces = num-spaces " "
    swap                                ||| stack: spaces, num-spaces
    Nat.>Int -2 * 21 + Int.>Nat-clamp   ||| stack: spaces, num-stars = 21 - 2 * num-spaces
    "*" repeat-string                   ||| stack: spaces, stars = num-stars "*"
    cat                                 ||| stack: spaces + stars
}

def main {
    ||| for n = -10 to 10:
    |||    print baklava-line(n)
    -10 10 range for(baklava-line print)
}

```

{% endraw %}

Baklava in [Mirth](https://sampleprograms.io/languages/mirth) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
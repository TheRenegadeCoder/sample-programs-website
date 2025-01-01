---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- gluon
title: Baklava in Gluon
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/gluon/how-to-implement-the-solution.md
- sources/programs/baklava/gluon/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Gluon](https://sampleprograms.io/languages/gluon) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gluon
let io @ { ? } = import! std.io
let int @ { ? } = import! std.int

rec let repeat_string s n : String -> Int -> String =
    if n > 0 then
        s ++ (repeat_string s (n - 1))
    else
        ""

let baklava_line n : Int -> String =
    let num_spaces = int.abs n
    let num_stars = 21 - 2 * num_spaces
    (repeat_string " " num_spaces) ++ (repeat_string "*" num_stars)

rec let baklava n ne : Int -> Int -> io.IO () =
    if n <= ne then
        io.println (baklava_line n)
        baklava (n + 1) ne
    else
        io.print ""

baklava -10 10

```

{% endraw %}

Baklava in [Gluon](https://sampleprograms.io/languages/gluon) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
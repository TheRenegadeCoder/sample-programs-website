---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- factor
title: Baklava in Factor
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/factor/how-to-implement-the-solution.md
- sources/programs/baklava/factor/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Factor](https://sampleprograms.io/languages/factor) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```factor
USING: io kernel math prettyprint ranges sequences ;
IN: baklava

! Based on https://rosettacode.org/wiki/Repeat_a_string#Factor
! but reversed arguments for fewer operations
: repeat-string ( n str -- str' ) <repetition> concat ;

: baklava-line ( n -- str )
    10 - abs        ! stack: num-spaces = abs(n - 10)
    dup             ! stack: num-spaces, num-spaces
    " "             ! stack: num-spaces, num-spaces, " "
    repeat-string   ! stack: num-spaces, spaces = " " num-spaces times
    swap            ! stack: spaces, num-spaces
    -2 * 21 +       ! stack: spaces, num-stars = 21 - 2 * num-spaces
    "*"             ! stack: spaces, num-stars, "*"
    repeat-string   ! stack: spaces, stars = "*" num-stars times
    append          ! stack: spaces + stars
    ;

! For n = 0 to 20, output Baklava line n
20 [0..b] [ baklava-line print ] each

```

{% endraw %}

Baklava in [Factor](https://sampleprograms.io/languages/factor) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
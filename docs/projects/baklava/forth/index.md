---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- forth
title: Baklava in Forth
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/forth/how-to-implement-the-solution.md
- sources/programs/baklava/forth/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Forth](https://sampleprograms.io/languages/forth) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```forth
: baklava
  ( for counter = -10 to 10 )
  11 -10 do
    i                       \ put outermost loop index on the stack
    abs                     \ num-spaces = abs(counter)
    dup spaces              \ output num-spaces " "
    -2 * 21 +               \ num-stars = 21 - 2 * num-spaces
    0 do [char] * emit loop \ for inner-counter = 0 to num-stars - 1, output "*"
                            \ Source: https://rosettacode.org/wiki/Loops/For#Forth
    cr
    loop ;

baklava
bye

```

{% endraw %}

Baklava in [Forth](https://sampleprograms.io/languages/forth) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
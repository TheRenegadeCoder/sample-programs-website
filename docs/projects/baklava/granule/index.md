---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- granule
title: Baklava in Granule
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/granule/how-to-implement-the-solution.md
- sources/programs/baklava/granule/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Granule](https://sampleprograms.io/languages/granule) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```granule
import Bool

repeatString : Int -> String[] -> String
repeatString 0 [str] = "";
repeatString times [str] = str `stringAppend` (repeatString (times - 1) [str])

numSpaces : Int[] -> Int
numSpaces [n] = if n < 0 then 0 - n else n

numStars : Int[] -> Int
numStars [n] = 21 - 2 * numSpaces [n]

baklavaLine : Int[] -> String
baklavaLine [n] =
    (repeatString (numSpaces [n]) [" "]) `stringAppend` (repeatString (numStars [n]) ["*"]) `stringAppend` "\n"

baklava : String[] -> Int[] -> Int[] -> String
baklava [lines] [n] [ne] =
    if n <= ne then
        lines `stringAppend` (baklavaLine [n]) `stringAppend` (baklava [lines] [n + 1] [ne])
    else
        lines

main : () <{Stdout}>
main = toStdout (baklava [""] [-10] [10])

```

{% endraw %}

Baklava in [Granule](https://sampleprograms.io/languages/granule) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
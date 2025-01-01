---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- idris
title: Baklava in Idris
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/idris/how-to-implement-the-solution.md
- sources/programs/baklava/idris/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Idris](https://sampleprograms.io/languages/idris) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```idris
module Main

repeatString : String -> Int -> String
repeatString s n = if n < 1 then "" else s ++ repeatString s (n - 1)

baklavaLine : Int -> String
baklavaLine n = repeatString " " numSpaces ++ repeatString "*" numStars
    where
        numSpaces = abs n
        numStars = 21 - 2 * numSpaces

main : IO ()
main = sequence_ $ map (putStrLn . baklavaLine) [-10..10]

```

{% endraw %}

Baklava in [Idris](https://sampleprograms.io/languages/idris) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
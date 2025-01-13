---
authors:
- rzuckerm
date: 2025-01-13
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-13
layout: default
tags:
- baklava
- eta
title: Baklava in Eta
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/eta/how-to-implement-the-solution.md
- sources/programs/baklava/eta/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Eta](https://sampleprograms.io/languages/eta) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```eta
module Main where

baklavaLine :: Int -> String
baklavaLine n = (replicate numSpaces ' ') ++ (replicate numStars '*') ++ "\n"
    where
        numSpaces = abs(n - 10)
        numStars = 21 - 2 * numSpaces

baklava :: String -> Int -> String
baklava s 0 = s ++ baklavaLine 0
baklava s n = s ++ baklavaLine n ++ baklava s (n - 1)

main :: IO ()
main = putStr (baklava "" 20)

```

{% endraw %}

Baklava in [Eta](https://sampleprograms.io/languages/eta) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
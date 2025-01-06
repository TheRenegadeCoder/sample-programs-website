---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- frege
title: Baklava in Frege
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/frege/how-to-implement-the-solution.md
- sources/programs/baklava/frege/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Frege](https://sampleprograms.io/languages/frege) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```frege
module Baklava where

main :: IO ()
main = putStr (baklava "" 20)

baklava :: String -> Int -> String
baklava s n
    | n < 0 = ""
    | otherwise = s ++ baklavaLine n ++ baklava s (n - 1)

baklavaLine :: Int -> String
baklavaLine n = do
    let num_spaces = abs (n - 10)
    let num_stars = 21 - 2 * num_spaces
    packed (replicate num_spaces ' ') ++ packed (replicate num_stars '*') ++ "\n"

```

{% endraw %}

Baklava in [Frege](https://sampleprograms.io/languages/frege) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
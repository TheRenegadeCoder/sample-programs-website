---
authors:
- rzuckerm
date: 2025-01-14
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-14
layout: default
tags:
- baklava
- discus
title: Baklava in Discus
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/discus/how-to-implement-the-solution.md
- sources/programs/baklava/discus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Discus](https://sampleprograms.io/languages/discus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```discus
module Main
import System.IO.Console
import Data.List
import Data.Text.List

where

baklavaLine (n: Nat): Text
 = (textOfCharList (replicate num_spaces ' ')) % (textOfCharList (replicate num_stars '*'))
    where
        num_spaces = if n > 10 then n - 10 else 10 -n
        num_stars = 21 - 2 * num_spaces

main ()
 =  forS (enumFromTo 0 20) $ λn
 -> writel $ baklavaLine n

```

{% endraw %}

Baklava in [Discus](https://sampleprograms.io/languages/discus) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
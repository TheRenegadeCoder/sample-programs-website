---
authors:
- Parker Johansen
date: 2018-10-20
featured-image: baklava-in-every-language.jpg
last-modified: 2019-03-26
layout: default
tags:
- baklava
- haskell
title: Baklava in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/haskell/how-to-implement-the-solution.md
- sources/programs/baklava/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

main :: IO ()
main = putStrLn baklava

-- Create baklava where the top has 10 spaces and then 1 asterisk
baklava ::  String
baklava = baklavaGrow 10 1

-- Recursively grow the baklava until spaces <= zero
baklavaGrow :: Int -> Int -> String
baklavaGrow space asterisk
  | space <= 0 = line 0     asterisk ++ "\n" ++ baklavaShrink 1          (asterisk - 2)
  | otherwise  = line space asterisk ++ "\n" ++ baklavaGrow   (space - 1) (asterisk + 2)

-- Recursively shrink the baklava until asterisks <= zero
baklavaShrink :: Int -> Int -> String
baklavaShrink space asterisk
  | asterisk <= 1 = line space 1
  | otherwise     = line space asterisk ++ "\n" ++ baklavaShrink (space + 1) (asterisk - 2)

-- Return a single line of the baklava
line space asterisk = replicate space ' ' ++ replicate asterisk '*'

```

{% endraw %}

Baklava in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
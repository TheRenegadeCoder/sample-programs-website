---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- purescript
title: Baklava in Purescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/purescript/how-to-implement-the-solution.md
- sources/programs/baklava/purescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Purescript](https://sampleprograms.io/languages/purescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```purescript
module Main where

import Prelude
import Effect (Effect)
import Effect.Console (log)

main :: Effect Unit
main = do
    baklava (-10) 10

baklava :: Int -> Int -> Effect Unit
baklava n ne
    | n > ne = pure unit
    | otherwise = do
        log (baklavaLine n)
        baklava (n + 1) ne

baklavaLine :: Int -> String
baklavaLine n = do
    let numSpaces = abs n
    let numStars = 21 - 2 * numSpaces
    (repeatString numSpaces " ") <> (repeatString numStars "*")

abs :: Int -> Int
abs n
    | n < 0 = -n
    | otherwise = n

repeatString :: Int -> String -> String
repeatString n s
    | n < 1 = ""
    | otherwise = s <> repeatString (n - 1) s

```

{% endraw %}

Baklava in [Purescript](https://sampleprograms.io/languages/purescript) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
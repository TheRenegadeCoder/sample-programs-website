---
authors:
- Jeremy Grifski
date: 2018-08-13
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-08-13
layout: default
tags:
- fizz-buzz
- haskell
title: Fizz Buzz in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/haskell/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

fizzbuzz :: Int -> String
fizzbuzz x
    | x `mod` 15 == 0 = "FizzBuzz"
    | x `mod` 3  == 0 = "Fizz"
    | x `mod` 5  == 0 = "Buzz"
    | otherwise       = show x

main = mapM (putStrLn . fizzbuzz) [1..100]

```

{% endraw %}

Fizz Buzz in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
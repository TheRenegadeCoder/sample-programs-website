---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-11
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- haskell
- palindromic-number
title: Palindromic Number in Haskell
title1: Palindromic
title2: Number in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/haskell/how-to-implement-the-solution.md
- sources/programs/palindromic-number/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where 

import Text.Read (readMaybe)
import Data.Maybe (listToMaybe)
import System.Environment

reverseInt :: Int -> Int
reverseInt n = go n 0
  where go 0 acc = acc
        go n acc = go (n `div` 10) (acc * 10 + n `mod` 10)

main :: IO ()
main = do  
    args <- getArgs
    case listToMaybe args >>= readMaybe of
      Just n  ->
        if n >= 0
        then putStrLn (if reverseInt n == n then "true" else "false") 
        else putStrLn "Usage: please input a non-negative integer"
      Nothing -> putStrLn "Usage: please input a non-negative integer"

```

{% endraw %}

Palindromic Number in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
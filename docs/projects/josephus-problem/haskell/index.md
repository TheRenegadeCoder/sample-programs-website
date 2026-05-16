---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-11
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- haskell
- josephus-problem
title: Josephus Problem in Haskell
title1: Josephus Problem
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/haskell/how-to-implement-the-solution.md
- sources/programs/josephus-problem/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Haskell](https://sampleprograms.io/languages/haskell)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Text.Read
import System.Environment

josephus :: Int -> Int -> Int
josephus 1 _ = 1
josephus n k = (josephus (n-1) k + k - 1) `mod` n + 1

parseArgs :: [String] -> Maybe (Int, Int)
parseArgs [n, k] = do
  n' <- readMaybe n
  k' <- readMaybe k
  return (n', k')
parseArgs _ = Nothing

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Just (n, k) -> print (josephus n k)
    Nothing     -> putStrLn "Usage: please input the total number of people and number of people to skip."

```

{% endraw %}

Josephus Problem in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
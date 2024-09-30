---
authors:
- Parker Johansen
date: 2018-11-16
featured-image: even-odd-in-every-language.jpg
last-modified: 2018-11-16
layout: default
tags:
- even-odd
- haskell
title: Even Odd in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/haskell/how-to-implement-the-solution.md
- sources/programs/even-odd/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

data EvenOdd = Even | Odd deriving (Show)

isEvenOdd :: Int -> EvenOdd
isEvenOdd x
  | x `mod` 2 == 0 = Even
  | otherwise  = Odd

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

main :: IO ()
main = do
  args <- getArgs
  let x = headMaybe args
  case x >>= readMaybe of
    Nothing -> putStrLn "Usage: please input a number"
    Just x  -> putStrLn $ show $ isEvenOdd x

```

{% endraw %}

Even Odd in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
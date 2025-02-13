---
authors:
- Parker Johansen
date: 2018-11-16
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-05-02
layout: default
tags:
- haskell
- prime-number
title: Prime Number in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/haskell/how-to-implement-the-solution.md
- sources/programs/prime-number/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

isPrime :: Integral a => a -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime x = null [n | n <- 2:[3,5..integralSqrt x], x `mod` n == 0]
  where integralSqrt = round . sqrt .fromIntegral

output :: Bool -> String
output True = "Prime"
output False = "Composite"

headMaybe :: [a] -> Maybe a
headMaybe [] = Nothing
headMaybe (x:xs) = Just x

main :: IO ()
main = do
  args <- getArgs
  let x = headMaybe args
  case x >>= readMaybe of
    Nothing -> putStrLn "Usage: please input a non-negative integer"
    Just x
      | x < 0       -> putStrLn "Usage: please input a non-negative integer"
      | otherwise   -> putStrLn $ output $ isPrime x

```

{% endraw %}

Prime Number in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
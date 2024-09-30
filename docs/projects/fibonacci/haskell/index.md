---
authors:
- Panagiotis Georgiadis
- Parker Johansen
date: 2018-10-15
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- fibonacci
- haskell
title: Fibonacci in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/haskell/how-to-implement-the-solution.md
- sources/programs/fibonacci/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

fibonacci :: Int -> [Integer]
fibonacci = flip (take) fibs

fibs :: [Integer]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

-- Takes a list of values and returns a list of strings in the format "ONE_BASED_INDEX: VALUE"
printWithIndex :: (Show a) => [a] -> [[Char]]
printWithIndex = zipWith (\i x -> (show i) ++ ": " ++ (show x)) [1..]


-- Prints out the first N numbers from the fibonacci sequence
-- where N equals to the first command line argument.
main :: IO ()
main = do
  args <- getArgs
  let n = headMaybe args
  case n >>= readMaybe of
    Nothing -> putStrLn "Usage: please input the count of fibonacci numbers to output"
    Just n  -> mapM_ (putStrLn) $ (printWithIndex . fibonacci) n

```

{% endraw %}

Fibonacci in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Panagiotis Georgiadis
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
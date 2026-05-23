---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-23
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-05-23
layout: default
tags:
- haskell
- zeckendorf
title: Zeckendorf in Haskell
title1: Zeckendorf
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/haskell/how-to-implement-the-solution.md
- sources/programs/zeckendorf/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](/projects/zeckendorf) in [Haskell](/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Data.Maybe (listToMaybe)
import Data.Function ((&))
import Data.List (intercalate)
import Control.Monad (guard)
import Text.Read (readMaybe)
import System.Environment (getArgs)

listToString :: [Int] -> String
listToString = intercalate ", " . map show

fib :: [Int]
fib = 1 : 1 : zipWith (+) fib (drop 1 fib)

zeckendorf :: Int -> [Int]
zeckendorf n =
  takeWhile (<= n) fib
  & foldr (\m (n, l) -> if m <= n then (n-m, m:l) else (n, l)) (n, [])
  & snd
  & reverse

parseArgs :: [String] -> Maybe Int
parseArgs args = do
  n  <- listToMaybe args
  n' <- readMaybe n
  guard (n' >= 0)
  return n'

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Nothing -> putStrLn "Usage: please input a non-negative integer"
    Just n  -> putStrLn $ listToString (zeckendorf n)


```

{% endraw %}

Zeckendorf in [Haskell](/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
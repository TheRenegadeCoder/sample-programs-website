---
authors:
- Ricardo Mapurunga Junior
date: 2026-04-29
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-04-29
layout: default
tags:
- haskell
- maximum-subarray
title: Maximum Subarray in Haskell
title1: Maximum Subarray
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/haskell/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

-- Converts string in format "1, 2, 3" to a Maybe list of int
stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

verifyListNotEmpty :: [a] -> Maybe [a]
verifyListNotEmpty [] = Nothing
verifyListNotEmpty xs = Just xs

main :: IO ()
main = do
  args <- getArgs
  let xs = headMaybe args >>= stringToListMaybe >>= verifyListNotEmpty
  case xs of
    Just xs -> print $ maximum $ scanr1 (\x acc -> if acc < 0 then x else x + acc)  xs
    Nothing -> putStrLn "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\""

```

{% endraw %}

Maximum Subarray in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
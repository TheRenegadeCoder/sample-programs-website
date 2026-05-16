---
authors:
- Ricardo Mapurunga Junior
date: 2026-04-29
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-04-29
layout: default
tags:
- haskell
- linear-search
title: Linear Search in Haskell
title1: Linear Search
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/haskell/how-to-implement-the-solution.md
- sources/programs/linear-search/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

-- Converts string in format "1, 2, 3" to a Maybe list of int
stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

-- Ensure that a list is not empty
verifyListLength :: [a] -> Maybe [a]
verifyListLength [] = Nothing
verifyListLength xs = Just xs

usage :: String
usage = "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"

main :: IO ()
main = do
  args <- getArgs
  case args of
    [xs, key] -> do
      let xs'  = stringToListMaybe xs >>= verifyListLength
      let key' = readMaybe key
      case elem <$> key' <*> xs' of
        Just res -> putStrLn (if res then "true" else "false")
        Nothing  -> putStrLn usage
    _         -> putStrLn usage

```

{% endraw %}

Linear Search in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- Ricardo Mapurunga Junior
date: 2026-04-29
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-04-29
layout: default
tags:
- haskell
- maximum-array-rotation
title: Maximum Array Rotation in Haskell
title1: Maximum Array
title2: Rotation in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/haskell/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read
import Data.List (tails)

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

verifyListNotEmpty :: [a] -> Maybe [a]
verifyListNotEmpty [] = Nothing
verifyListNotEmpty xs = Just xs

-- get all rotated versions of the list xs
rotations :: [a] -> [[a]]
rotations xs =
  let n = length xs
  in take n $ map (take n) $ tails (cycle xs)

main :: IO ()
main = do
  args <- getArgs
  let xs = headMaybe args >>= stringToListMaybe >>= verifyListNotEmpty
  case xs of
    Just xs -> print $ maximum $ map (sum . zipWith (*) [0..]) $ rotations xs
    Nothing -> putStrLn "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")"
  

```

{% endraw %}

Maximum Array Rotation in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
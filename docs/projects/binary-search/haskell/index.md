---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-11
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- binary-search
- haskell
title: Binary Search in Haskell
title1: Binary Search
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/haskell/how-to-implement-the-solution.md
- sources/programs/binary-search/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](/projects/binary-search) in [Haskell](/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Data.Array (Array, (!))
import qualified Data.Array as Array
import Control.Monad (guard)
import Text.Read

-- Converts string in format "1, 2, 3" to a Maybe array of int
stringToArrayMaybe :: String -> Maybe (Array Int Int)
stringToArrayMaybe str = do
  xs <- readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]
  guard $ (not . null) xs
  return $ Array.listArray (0, length xs - 1) xs

isSorted :: (Ord a) => [a] -> Bool
isSorted []         = True
isSorted [_]        = True
isSorted (x1:x2:xs) = x1 <= x2 && isSorted (x2:xs)

parseArgs :: [String] -> Maybe (Array Int Int, Int)
parseArgs [a, t] = do
  target <- readMaybe t
  array  <- stringToArrayMaybe a
  guard (isSorted (Array.elems array))
  return (array, target)
parseArgs _      = Nothing

binarySearch :: (Ord e) => e -> Array Int e -> Bool
binarySearch x xs = go lo hi
  where
  (lo, hi) = Array.bounds xs
  go l h
    | l > h       = False
    | xs ! m == x = True
    | xs ! m < x  = go (m+1) h
    | otherwise   = go l (m-1)
    where m = (h+l) `quot` 2

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Nothing ->
      putStrLn "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"
    Just (array, target) ->
      let result = binarySearch target array
      in  putStrLn (if result then "true" else "false")


```

{% endraw %}

Binary Search in [Haskell](/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
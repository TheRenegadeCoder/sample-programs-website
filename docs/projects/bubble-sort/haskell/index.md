---
authors:
- Parker Johansen
date: 2018-12-02
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-03-26
layout: default
tags:
- bubble-sort
- haskell
title: Bubble Sort in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/haskell/how-to-implement-the-solution.md
- sources/programs/bubble-sort/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Text.Read
import System.Environment
import System.Exit (exitWith, ExitCode(ExitFailure))
import Data.List (intercalate)


bubble :: Ord a => [a] -> [a]
bubble xs = foldl (\acc _ -> pass acc) xs xs
  where pass [x] = [x]
        pass (x1:x2:xs)
          | x1 > x2   = x2:(pass (x1:xs))
          | otherwise = x1:(pass (x2:xs))


headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

-- Converts string in format "1, 2, 3" to a Maybe list of int
stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

-- Ensure that a list contains at least two elements
verifyListLength :: Ord a => [a] -> Maybe [a]
verifyListLength []     = Nothing
verifyListLength [x]    = Nothing
verifyListLength (x:xs) = Just (x:xs)

listToString :: [Int] -> String
listToString = intercalate ", " . map show


main :: IO ()
main = do
  args <- getArgs
  let xs = headMaybe args >>= stringToListMaybe >>= verifyListLength
  case xs of
    Nothing -> do
      putStrLn "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""
      exitWith $ ExitFailure 1
    Just xs  -> putStrLn $ listToString $ bubble xs


```

{% endraw %}

Bubble Sort in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
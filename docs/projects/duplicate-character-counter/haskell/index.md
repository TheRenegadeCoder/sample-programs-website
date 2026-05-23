---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-23
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-23
layout: default
tags:
- duplicate-character-counter
- haskell
title: Duplicate Character Counter in Haskell
title1: Duplicate Character
title2: Counter in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/haskell/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](/projects/duplicate-character-counter) in [Haskell](/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
{-# LANGUAGE TupleSections #-}

module Main where

import Data.Map (Map)
import qualified Data.Map.Strict as Map
import System.Environment (getArgs)

duplicateCharacters :: String -> Map Char Int
duplicateCharacters = Map.filter (> 1) . Map.fromListWith (+) . map (, 1)

printDuplicates :: String -> Map Char Int -> IO ()
printDuplicates []     _ = return ()
printDuplicates (x:xs) m =
  case Map.updateLookupWithKey (\_ _ -> Nothing) x m of
    (Just count, m') -> putStrLn (x : ": " ++ show count) >> printDuplicates xs m'
    _                -> printDuplicates xs m

main :: IO ()
main = do
  args <- getArgs
  case args of
    [xs@(_:_)] ->
      let m = duplicateCharacters xs
      in if Map.null m
          then putStrLn "No duplicate characters"
          else printDuplicates xs m
    _          -> putStrLn "Usage: please provide a string"


```

{% endraw %}

Duplicate Character Counter in [Haskell](/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
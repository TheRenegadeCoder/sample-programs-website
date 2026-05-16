---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-11
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- haskell
- transpose-matrix
title: Transpose Matrix in Haskell
title1: Transpose Matrix
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/haskell/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Haskell](https://sampleprograms.io/languages/haskell)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell

module Main where

import System.Environment
import Text.Read
import Data.List (transpose, intercalate)
import Data.Function ((&))
import Control.Monad (guard)

-- Converts string in format "1, 2, 3" to a Maybe list of int
stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

listToMatrix :: Int -> [Int] -> [[Int]]
listToMatrix _ [] = []
listToMatrix n l  = let (row, xs) = splitAt n l in row : listToMatrix n xs

listToString :: (Show a) => [a] -> String
listToString = intercalate ", " . map show

parseArgs :: [String] -> Maybe (Int, Int, [Int])
parseArgs [cols, rows, list] = do
  cols' <- readMaybe cols
  rows' <- readMaybe rows
  list' <- stringToListMaybe list
  guard $ cols' > 0 && rows' > 0 && cols' * rows' == length list'
  return (cols', rows', list')
parseArgs _ = Nothing

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Nothing        -> putStrLn "Usage: please enter the dimension of the matrix and the serialized matrix"
    Just (c, _, l) -> listToMatrix c l & transpose & concat & listToString & putStrLn

```

{% endraw %}

Transpose Matrix in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-23
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-05-23
layout: default
tags:
- convex-hull
- haskell
title: Convex Hull in Haskell
title1: Convex Hull
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/haskell/how-to-implement-the-solution.md
- sources/programs/convex-hull/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](/projects/convex-hull) in [Haskell](/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Data.List (minimumBy, maximumBy)
import Data.Ord (comparing)
import Control.Monad (guard, forM_)
import Text.Read (readMaybe)
import System.Environment (getArgs)

type Point = (Int, Int)

stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

cross :: Point -> Point -> Point -> Int
cross (x1, y1) (x2, y2) (x3, y3) = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

dist :: Point -> Point -> Int
dist (x1, y1) (x2, y2) = (x2 - x1) ^ 2 + (y2 - y1) ^ 2

jarvis :: [Point] -> [Point]
jarvis points = startingPoint : go startingPoint
  where
  startingPoint  = minimumBy (comparing fst) points 
  nextPoint prev = maximumBy (comparePoints prev) points
  comparePoints prev p1 p2 =
    case compare (cross prev p1 p2) 0 of
      EQ -> compare (dist prev p1) (dist prev p2)
      x  -> x
  go cur
    | next == startingPoint = []
    | otherwise             = next : go next
    where next = nextPoint cur

parseArgs :: [String] -> Maybe [Point]
parseArgs [xs, ys] = do
  xs' <- stringToListMaybe xs
  ys' <- stringToListMaybe ys
  guard (length xs' > 2  && length xs' == length ys')
  return (zip xs' ys')
parseArgs _ = Nothing

printPoint :: Point -> IO ()
printPoint (x, y) = putStrLn $ "(" ++ show x ++ ", " ++ show y ++ ")"

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Nothing -> putStrLn "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. \"100, 440, 210\")"
    Just coords -> forM_ (jarvis coords) printPoint

```

{% endraw %}

Convex Hull in [Haskell](/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
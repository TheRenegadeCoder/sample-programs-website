---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-18
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-18
layout: default
tags:
- haskell
- minimum-spanning-tree
title: Minimum Spanning Tree in Haskell
title1: Minimum Spanning
title2: Tree in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/haskell/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Data.Array (Array, (!))
import qualified Data.Array as Array
import Text.Read (readMaybe)
import Control.Monad (guard)
import Data.IntSet (IntSet)
import qualified Data.IntSet as IS
import Data.Set (Set)
import qualified Data.Set as Set
import System.Environment

stringToListMaybe :: String -> Maybe [Int]
stringToListMaybe str = readMaybe $ "[" ++ str ++ "]" :: Maybe [Int]

chunksOf :: Int -> [Int] -> [[Int]]
chunksOf _ [] = []
chunksOf n l  = let (row, xs) = splitAt n l in row : chunksOf n xs

buildAdjacencyMatrix :: [Int] -> Array Int [Int]
buildAdjacencyMatrix l = Array.listArray (0, n-1) (chunksOf n l)
  where
  n = round (sqrt (fromIntegral (length l))) -- size of a row in a square matrix

prim :: Array Int [Int] -> Int
prim adj = go IS.empty (Set.singleton (0, 0))
  where 
  go vis pq
    | Set.null pq = 0
    | otherwise   =
        let ((weight, v), pq') = Set.deleteFindMin pq
        in if IS.member v vis
           then go vis pq'
           else 
             let pq'' = foldr Set.insert pq' (unvisitedEdges v vis)
             in weight + go (IS.insert v vis) pq''
  unvisitedEdges v vis =
    [ (weight, u)
    | (weight, u) <- zip (adj ! v) [0..]
    , weight /= 0, u `IS.notMember` vis
    ]
      
parseArgs :: [String] -> Maybe [Int]
parseArgs [l] = do
  l <- stringToListMaybe l 
  guard $ (not . null) l && isSquare (length l)
  return l
  where isSquare n = (round $ sqrt $ fromIntegral n) ^ 2 == n
parseArgs _ = Nothing

main :: IO ()
main = do
  args <- getArgs
  case parseArgs args of
    Nothing -> putStrLn "Usage: please provide a comma-separated list of integers"
    Just l  -> print $ prim (buildAdjacencyMatrix l)

```

{% endraw %}

Minimum Spanning Tree in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
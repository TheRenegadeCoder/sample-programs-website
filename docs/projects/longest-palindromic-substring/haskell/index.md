---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-11
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-11
layout: default
tags:
- haskell
- longest-palindromic-substring
title: Longest Palindromic Substring in Haskell
title1: Longest Palindromic
title2: Substring in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/haskell/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Data.List (maximumBy, tails, inits)
import Data.Maybe (listToMaybe)
import Data.Function ((&))
import Data.Ord (comparing)

substrings :: [a] -> [[a]]
substrings = concatMap tails . inits

longestPalindromicSubstring :: String -> Maybe String
longestPalindromicSubstring str =
  case palindromes of
    [] -> Nothing
    _  -> Just $ maximumBy (comparing length) palindromes
  where palindromes = substrings str & filter (\s -> length s > 1 && reverse s == s)

main :: IO ()
main = do
  args <- getArgs
  case listToMaybe args >>= longestPalindromicSubstring of
    Nothing  -> putStrLn "Usage: please provide a string that contains at least one palindrome"
    Just res -> putStrLn res

```

{% endraw %}

Longest Palindromic Substring in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- Ricardo Mapurunga Junior
date: 2026-04-29
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-04-29
layout: default
tags:
- haskell
- remove-all-whitespace
title: Remove All Whitespace in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/haskell/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Data.Char (isSpace)
import System.Environment

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

verifyStringNotEmpty :: String -> Maybe String
verifyStringNotEmpty "" = Nothing
verifyStringNotEmpty xs = Just xs

main :: IO ()
main = do
  args <- getArgs
  let inputStr = headMaybe args >>= verifyStringNotEmpty
  case inputStr of
    Just str -> putStrLn $ filter (not . isSpace) str
    Nothing  -> putStrLn "Usage: please provide a string"

```

{% endraw %}

Remove All Whitespace in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
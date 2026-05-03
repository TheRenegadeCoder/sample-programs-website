---
authors:
- Ricardo Mapurunga Junior
date: 2026-04-29
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-04-29
layout: default
tags:
- haskell
- longest-word
title: Longest Word in Haskell
title1: Longest Word
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/haskell/how-to-implement-the-solution.md
- sources/programs/longest-word/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Data.Function ((&))

usage :: String
usage = "Usage: please provide a string"

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
    Just str -> str & words & map length & maximum & print
    Nothing  -> putStrLn "Usage: please provide a string"

```

{% endraw %}

Longest Word in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
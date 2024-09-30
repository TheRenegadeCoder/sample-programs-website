---
authors:
- Amanda Eubanks
- Jeremy Grifski
date: 2019-10-13
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- haskell
title: Capitalize in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/haskell/how-to-implement-the-solution.md
- sources/programs/capitalize/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where 

import Data.Char
import System.Environment

capitalize :: String -> String
capitalize (head:tail) = toUpper head : tail
capitalize [] = []

main = do  
    args <- getArgs
    case args of
      [inputStr] -> case inputStr of
        [] -> putStrLn "Usage: please provide a string"
        _  -> putStrLn $ capitalize inputStr
      _          -> putStrLn "Usage: please provide a string"

```

{% endraw %}

Capitalize in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Amanda Eubanks
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
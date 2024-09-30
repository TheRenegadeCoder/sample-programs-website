---
authors:
- Parker Johansen
date: 2018-11-20
featured-image: rot13-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- haskell
- rot13
title: Rot13 in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/haskell/how-to-implement-the-solution.md
- sources/programs/rot13/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import Data.Char
import System.Environment
import System.Exit (exitWith, ExitCode(ExitFailure))

rot13 :: String -> String
rot13 = map encryptChar

encryptChar :: Char -> Char
encryptChar c
  | ord c >= 65 && ord c <= 90  = toChar 65 $ addDigits $ toNum 65 c
  | ord c >= 97 && ord c <= 122 = toChar 97 $ addDigits $ toNum 97 c
  | otherwise = c
    where toNum base c = (ord c) - base
          toChar base n = chr $ n + base
          addDigits n = (n + 13) `mod` 26



main :: IO ()
main = do
  args <- getArgs
  if null args || (head args) == "" then do
    putStrLn "Usage: please provide a string to encrypt"
    exitWith $ ExitFailure 1
  else
    putStrLn $ rot13 $ head args

```

{% endraw %}

Rot13 in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
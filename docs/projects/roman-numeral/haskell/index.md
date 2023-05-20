---
title: Roman Numeral in Haskell
layout: default
date: 2018-10-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2018-10-21

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import System.Exit (exitWith, ExitCode(ExitFailure))

asDec :: Char -> Int
asDec 'I' = 1
asDec 'V' = 5
asDec 'X' = 10
asDec 'L' = 50
asDec 'C' = 100
asDec 'D' = 500
asDec 'M' = 1000
asDec _   = -1

romanToDecimal :: String -> Maybe Int
romanToDecimal roman = go roman 0
    where go :: String -> Int -> Maybe Int
          go []  totals  = Just totals
          go [a] totals  = Just $ totals + (asDec a)
          go (a1:a2:as) totals
            | (asDec a1) < 1 ||  (asDec a2) < 1 = Nothing
            | (asDec a1) < (asDec a2)           = go (a2:as) (totals - (asDec a1))
            | otherwise                         = go (a2:as) (totals + (asDec a1))


main :: IO ()
main = do
  args <- getArgs
  let roman = head args
  if null args then do
    putStrLn "Usage: please provide a string of roman numerals"
    exitWith $ ExitFailure 1
  else do
    let intOut = romanToDecimal roman
    case intOut of
      Nothing -> do
        putStrLn "Error: invalid string of roman numerals"
        exitWith $ ExitFailure 1
      Just x -> putStrLn $ show $ x
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 01 2019 03:55:34. The solution was first committed on Oct 21 2018 01:06:56. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
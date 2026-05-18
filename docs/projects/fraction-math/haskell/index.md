---
authors:
- Ricardo Mapurunga Junior
date: 2026-05-18
featured-image: fraction-math-in-every-language.jpg
last-modified: 2026-05-18
layout: default
tags:
- fraction-math
- haskell
title: Fraction Math in Haskell
title1: Fraction Math
title2: in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/haskell/how-to-implement-the-solution.md
- sources/programs/fraction-math/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read
import Data.Bifunctor (second)
import Data.Ratio

parseOperator :: String -> Maybe (Rational -> Rational -> Rational)
parseOperator op = lookup op operators
  where
  -- converts relational operations that return bool, to operations that return rationals - 1 for True, 0 for False
  relationalToRational f a b = toRational $ fromEnum (f a b)
  arithmeticOps = [("+", (+)), ("-", (-)), ("/", (/)), ("*", (*))]
  relationalOps = [(">", (>)), ("<", (<)), (">=", (>=)), ("<=", (<=)), ("==", (==)), ("!=", (/=))]
  operators = arithmeticOps ++ map (second relationalToRational) relationalOps

parseFraction :: String -> Maybe Rational
parseFraction s = do
  let (num, den) = break (== '/') s
  num' <- readMaybe num
  den' <- readMaybe (drop 1 den) -- drop 1 for the '/'
  return (num' % den')

applyOperator :: [String] -> Maybe Rational
applyOperator [frac1, op, frac2] = do
  operand1 <- parseFraction frac1
  operand2 <- parseFraction frac2
  operator <- parseOperator op
  return (operand1 `operator` operand2)
applyOperator _ = Nothing

rationalToString :: Rational -> String
rationalToString x
  | denominator x == 1 = show (numerator x)
  | otherwise          = show (numerator x) ++ "/" ++ show (denominator x)

main :: IO ()
main = do
  args <- getArgs
  case applyOperator args of
    Just res -> putStrLn (rationalToString res)
    Nothing  -> putStrLn "Usage: ./fraction-math operand1 operator operand2"

```

{% endraw %}

Fraction Math in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Ricardo Mapurunga Junior

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
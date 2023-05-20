---
title: Factorial in Haskell
layout: default
date: 2018-11-16
featured-image: factorial-in-every-language.jpg
last-modified: 2018-11-16

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment
import Text.Read

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

headMaybe :: [a] -> Maybe a
headMaybe [] = Nothing
headMaybe (x:xs) = Just x

main :: IO ()
main = do
  args <- getArgs
  let n = headMaybe args
  case n >>= readMaybe of
    Nothing -> putStrLn "Usage: please input a non-negative integer"
    Just n
      | n < 0       -> putStrLn "Usage: please input a non-negative integer"
      | n <= 250000 -> putStrLn $ take 10 $ show $ factorial n
      | otherwise   -> putStrLn $ "!" ++ (show n) ++ " is out of the reasonable bounds for calculation"
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
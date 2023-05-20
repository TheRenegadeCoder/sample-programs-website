---
title: Reverse String in Haskell
layout: default
date: 2018-10-17
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-10-17

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

import System.Environment

main :: IO ()
main = do
  args <- getArgs
  if null args then
    putStrLn ""
  else
    putStrLn $ reverse $ head args
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Panagiotis Georgiadis
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 17 2018 10:53:21. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
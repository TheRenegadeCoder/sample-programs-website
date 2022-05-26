---

title: Reverse String in Haskell
layout: default
date: 2022-04-28
last-modified: 2022-05-26

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
    error "You need to provide us with a string in order to reverse it"
  else
    putStrLn $ reverse $ head args
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Panagiotis Georgiadis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---

title: Reverse String in Haskell
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Reverse String in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Reverse String in Haskell was written by:

- Panagiotis Georgiadis

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
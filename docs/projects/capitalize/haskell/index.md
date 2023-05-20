---
title: Capitalize in Haskell
layout: default
date: 2019-10-13
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-13

---

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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Amanda Eubanks
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 23:11:24. The solution was first committed on Oct 13 2019 17:52:43. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
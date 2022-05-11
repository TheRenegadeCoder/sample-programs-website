---

title: Fizz Buzz in Haskell
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```haskell
module Main where

fizzbuzz :: Int -> String
fizzbuzz x
    | x `mod` 15 == 0 = "FizzBuzz"
    | x `mod` 3  == 0 = "Fizz"
    | x `mod` 5  == 0 = "Buzz"
    | otherwise       = show x

main = mapM (putStrLn . fizzbuzz) [1..100]
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
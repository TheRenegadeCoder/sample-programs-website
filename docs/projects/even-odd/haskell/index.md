---

title: Even Odd in Haskell
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Haskell
module Main where

import System.Environment
import Text.Read

data EvenOdd = Even | Odd deriving (Show)

isEvenOdd :: Int -> EvenOdd
isEvenOdd x
  | x `mod` 2 == 0 = Even
  | otherwise  = Odd

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

main :: IO ()
main = do
  args <- getArgs
  let x = headMaybe args
  case x >>= readMaybe of
    Nothing -> putStrLn "Usage: please input a number"
    Just x  -> putStrLn $ show $ isEvenOdd x
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
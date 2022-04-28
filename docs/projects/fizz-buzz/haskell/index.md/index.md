---

---

# Fizz Buzz in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
module Main where

fizzbuzz :: Int -> String
fizzbuzz x
    | x `mod` 15 == 0 = "FizzBuzz"
    | x `mod` 3  == 0 = "Fizz"
    | x `mod` 5  == 0 = "Buzz"
    | otherwise       = show x

main = mapM (putStrLn . fizzbuzz) [1..100]

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
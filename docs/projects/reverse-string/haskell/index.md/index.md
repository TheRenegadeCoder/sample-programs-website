# Reverse String in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
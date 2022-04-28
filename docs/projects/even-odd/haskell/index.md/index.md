# Even Odd in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
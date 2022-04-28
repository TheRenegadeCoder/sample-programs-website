---

---

# Fibonacci in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
module Main where

import System.Environment
import Text.Read

fibonacci :: Int -> [Integer]
fibonacci = flip (take) fibs

fibs :: [Integer]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

headMaybe :: [a] -> Maybe a
headMaybe []     = Nothing
headMaybe (x:xs) = Just x

-- Takes a list of values and returns a list of strings in the format "ONE_BASED_INDEX: VALUE"
printWithIndex :: (Show a) => [a] -> [[Char]]
printWithIndex = zipWith (\i x -> (show i) ++ ": " ++ (show x)) [1..]


-- Prints out the first N numbers from the fibonacci sequence
-- where N equals to the first command line argument.
main :: IO ()
main = do
  args <- getArgs
  let n = headMaybe args
  case n >>= readMaybe of
    Nothing -> putStrLn "Usage: please input the count of fibonacci numbers to output"
    Just n  -> mapM_ (putStrLn) $ (printWithIndex . fibonacci) n

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
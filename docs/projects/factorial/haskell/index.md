---

title: Factorial in Haskell

---

Welcome to the Factorial in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Haskell
module Main where

import System.Environment
import Text.Read

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

headMaybe :: [a] -> Maybe a
headMaybe [] = Nothing
headMaybe (x:xs) = Just x

main :: IO ()
main = do
  args <- getArgs
  let n = headMaybe args
  case n >>= readMaybe of
    Nothing -> putStrLn "Usage: please input a non-negative integer"
    Just n
      | n < 0       -> putStrLn "Usage: please input a non-negative integer"
      | n <= 250000 -> putStrLn $ take 10 $ show $ factorial n
      | otherwise   -> putStrLn $ "!" ++ (show n) ++ " is out of the reasonable bounds for calculation"

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
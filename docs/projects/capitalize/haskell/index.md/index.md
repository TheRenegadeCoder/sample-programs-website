---

---

# Capitalize in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
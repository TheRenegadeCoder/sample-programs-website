---

title: Capitalize in Haskell

---

Welcome to the Capitalize in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
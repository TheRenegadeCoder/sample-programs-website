---

---

Welcome to the Reverse String in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
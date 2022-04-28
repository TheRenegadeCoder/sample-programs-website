---

---

# Rot 13 in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
module Main where

import Data.Char
import System.Environment
import System.Exit (exitWith, ExitCode(ExitFailure))

rot13 :: String -> String
rot13 = map encryptChar

encryptChar :: Char -> Char
encryptChar c
  | ord c >= 65 && ord c <= 90  = toChar 65 $ addDigits $ toNum 65 c
  | ord c >= 97 && ord c <= 122 = toChar 97 $ addDigits $ toNum 97 c
  | otherwise = c
    where toNum base c = (ord c) - base
          toChar base n = chr $ n + base
          addDigits n = (n + 13) `mod` 26



main :: IO ()
main = do
  args <- getArgs
  if null args || (head args) == "" then do
    putStrLn "Usage: please provide a string to encrypt"
    exitWith $ ExitFailure 1
  else
    putStrLn $ rot13 $ head args

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
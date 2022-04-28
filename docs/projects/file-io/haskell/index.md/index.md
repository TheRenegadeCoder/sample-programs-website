---

---

Welcome to the File Io in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
module Main where

import System.IO

main :: IO ()
main = do
  -- write
  handle <- openFile "output.txt" ReadWriteMode
  hPutStr handle "file contents"
  hClose handle
  -- read
  handle <- openFile "output.txt" ReadWriteMode
  value <- hGetContents handle
  -- Print the contents of the file that was read.
  -- Haskell reads the file lazily, so the value must be printed before the handle is closed
  putStrLn value
  hClose handle

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.
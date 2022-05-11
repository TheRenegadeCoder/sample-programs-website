---

title: File Io in Haskell
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the File Io in Haskell page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
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

{% endraw %}

File Io in Haskell was written by:

- Parker Johansen

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 24 2018 10:42:45. The solution was first committed on Oct 22 2018 09:07:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- Parker Johansen
date: 2018-10-22
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-10-24
layout: default
tags:
- file-input-output
- haskell
title: File Input Output in Haskell
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/haskell/how-to-implement-the-solution.md
- sources/programs/file-input-output/haskell/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

File Input Output in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- manasmithamn
date: 2020-10-25
featured-image: file-input-output-in-every-language.jpg
last-modified: 2020-10-25
layout: default
tags:
- file-input-output
- r
title: File Input Output in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/r/how-to-implement-the-solution.md
- sources/programs/file-input-output/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r

file_create_result = tryCatch({
#Open and write 2 lines to the file.
  fileConn<-file("output.txt")
  writeLines(c("Hello","World\n"), fileConn)
  writeLines(c("Writing this file using R"), fileConn)
  close(fileConn)
},
 warning = function( w )
  {
     cat("Warning while opening the file")
  },
   error = function( w )
  {
     cat("Error while opening the file")
  }
)
# Catch File Open Error
if(file.exists("output.txt")){
  f_open = readLines("output.txt")
  singleString <- paste(readLines("output.txt"), collapse=" ")
  cat(singleString)
} else{
  cat("File doesn't exist")
}

```

{% endraw %}

File Input Output in [R](https://sampleprograms.io/languages/r) was written by:

- manasmithamn

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
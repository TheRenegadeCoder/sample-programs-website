---
authors:
- rzuckerm
date: 2023-09-16
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-09-16
layout: default
tags:
- commodore-basic
- file-input-output
title: File Input Output in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/commodore-basic/how-to-implement-the-solution.md
- sources/programs/file-input-output/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
10 OPEN 1, 1, 1, "output.txt"
20 PRINT#1, "Hello from Commodore Basic"
30 PRINT#1, "This is a line"
40 PRINT#1, "This is another line"
50 PRINT#1, "Goodbye!"
60 CLOSE 1
70 OPEN 1, 1, 0, "output.txt"
80 INPUT#1, A$
90 PRINT A$
100 IF ST = 0 THEN GOTO 80
110 CLOSE 1

```

{% endraw %}

File Input Output in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
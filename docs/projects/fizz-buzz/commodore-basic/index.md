---
authors:
- rzuckerm
date: 2023-09-13
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-09-13
layout: default
tags:
- commodore-basic
- fizz-buzz
title: Fizz Buzz in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/commodore-basic/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
10 FOR I = 1 TO 100
20     S$ = ""
30     IF (I - INT(I / 3) * 3) = 0 THEN S$ = S$ + "Fizz"
40     IF (I - INT(I / 5) * 5) = 0 THEN S$ = S$ + "Buzz"
45     REM STR$(I) prepends a space for positive numbers. MID$ removes it
50     IF S$ = "" THEN S$ = S$ + MID$(STR$(I), 2)
60     PRINT S$
70 NEXT I

```

{% endraw %}

Fizz Buzz in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2023-09-16
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-09-16
layout: default
tags:
- commodore-basic
- reverse-string
title: Reverse String in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/commodore-basic/how-to-implement-the-solution.md
- sources/programs/reverse-string/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
5 REM Input string
10 GOSUB 1000
20 R$ = ""
30 IF S$ = "" THEN GOTO 70
40 FOR K = LEN(S$) TO 1 STEP -1
50     R$ = R$ + MID$(S$, K, 1)
60 NEXT K
70 PRINT R$
80 END
1000 REM Read input value one character at a time since Commodore BASIC
1001 REM has trouble reading line from stdin properly
1002 REM S$ = string
1003 REM Initialize
1010 S$ = ""
1015 REM Append characters until end of value or input
1020 GET A$
1030 C = ASC(A$)
1040 IF C = 13 OR C = 255 THEN RETURN: REM end of value or input
1050 S$ = S$ + A$
1060 GOTO 1020

```

{% endraw %}

Reverse String in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
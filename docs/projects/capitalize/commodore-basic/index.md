---
authors:
- rzuckerm
date: 2023-09-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-09-17
layout: default
tags:
- capitalize
- commodore-basic
title: Capitalize in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/commodore-basic/how-to-implement-the-solution.md
- sources/programs/capitalize/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
5 REM Input string
10 GOSUB 1000
20 IF S$ = "" THEN GOTO 80
30 R1$ = LEFT$(S$, 1)
40 IF R1$ >= "a" AND R1$ <= "z" THEN R1$ = CHR$(ASC(R1$) - 32)
50 R$ = R1$ + MID$(S$, 2)
60 PRINT R$
70 END
80 PRINT "Usage: please provide a string"
90 END
1000 REM Read input value one character at a time since Commodore BASIC
1001 REM has trouble reading line from stdin properly
1002 REM S$ = string
1003 REM Initialize
1010 S$ = ""
1015 REM Append characters until end of input
1020 GET A$
1030 C = ASC(A$)
1040 IF C = 13 OR C = 255 THEN RETURN: REM end of value or input
1050 S$ = S$ + A$
1060 GOTO 1020

```

{% endraw %}

Capitalize in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2023-09-17
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-09-17
layout: default
tags:
- commodore-basic
- remove-all-whitespace
title: Remove All Whitespace in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/commodore-basic/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
5 REM Input string
10 GOSUB 1000
20 R$ = ""
30 IF S$ = "" OR S$ = CHR$(13) THEN GOTO 120
40 FOR K = 1 TO LEN(S$)
50     A$ = MID$(S$, K, 1)
60     IF A$ = CHR$(9) OR A$ = CHR$(10) OR A$ = CHR$(13) THEN GOTO 90
70     IF A$ = " " THEN GOTO 90: REM Can't put on above line, too long
80     R$ = R$ + A$
90 NEXT K
100 PRINT R$
110 END
120 PRINT "Usage: please provide a string"
130 END
1000 REM Read input value one character at a time since Commodore BASIC
1001 REM has trouble reading line from stdin properly
1002 REM S$ = string
1003 REM Initialize
1010 S$ = ""
1015 REM Append characters until end of input
1020 GET A$
1030 C = ASC(A$)
1040 IF C = 255 THEN RETURN: REM end of input
1050 S$ = S$ + A$
1060 GOTO 1020

```

{% endraw %}

Remove All Whitespace in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
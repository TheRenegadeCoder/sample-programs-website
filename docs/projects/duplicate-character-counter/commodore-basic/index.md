---
authors:
- rzuckerm
date: 2023-09-16
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-10-15
layout: default
tags:
- commodore-basic
- duplicate-character-counter
title: Duplicate Character Counter in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/commodore-basic/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
10 DIM CC%(255): REM character counter
15 REM Input string
20 GOSUB 1000
30 IF S$ = "" THEN GOTO 200
35 REM Count characters
40 L% = LEN(S$)
50 FOR K = 1 TO L%
60     CN% = ASC(MID$(S$, K, 1))
70     CC%(CN%) = CC%(CN%) + 1
80 NEXT K
85 REM Show duplicate character counts
90 DP% = 0
100 FOR K = 1 TO L%
110     A$ = MID$(S$, K, 1)
120     CN% = ASC(A$)
130     IF CC%(CN%) < 2 THEN GOTO 170
140     PRINT A$; ": "; MID$(STR$(CC%(CN%)), 2)
150     CC%(CN%) = 0: REM indicate character displayed
160     DP% = 1
170 NEXT K
180 IF DP% = 0 THEN PRINT "No duplicate characters"
190 END
200 PRINT "Usage: please provide a string"
210 END
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

Duplicate Character Counter in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
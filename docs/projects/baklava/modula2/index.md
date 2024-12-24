---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- modula2
title: Baklava in Modula2
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/modula2/how-to-implement-the-solution.md
- sources/programs/baklava/modula2/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Modula2](https://sampleprograms.io/languages/modula2) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```modula2
MODULE Baklava;

FROM StrIO IMPORT WriteString, WriteLn;

PROCEDURE WriteRepeatString(s: ARRAY OF CHAR; n: CARDINAL);
VAR i: CARDINAL;
BEGIN
    FOR i := 1 TO n DO
        WriteString(s);
    END
END WriteRepeatString;

VAR
    n: INTEGER;
    numSpaces: CARDINAL;
    numStars: CARDINAL;

BEGIN
    FOR n := -10 TO 10 DO
        numSpaces := ABS(n);
        numStars := 21 - 2 * numSpaces;
        WriteRepeatString(' ', numSpaces);
        WriteRepeatString('*', numStars);
        WriteLn;
    END;
END Baklava.

```

{% endraw %}

Baklava in [Modula2](https://sampleprograms.io/languages/modula2) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
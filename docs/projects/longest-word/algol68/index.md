---
authors:
- rzuckerm
date: 2023-01-24
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-01-31
layout: default
tags:
- algol68
- longest-word
title: Longest Word in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/algol68/how-to-implement-the-solution.md
- sources/programs/longest-word/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string"));

PROC longest word length = (STRING s) INT:
(
    INT longest word len := 0;
    INT word len := 0;
    FOR n TO UPB s
    DO
        # If whitespace, reset word length #
        IF isspace(s[n])
        THEN
            word len := 0
        # Else increment word length and update longest word length #
        ELSE
            word len +:= 1;
            IF word len > longest word len
            THEN
                longest word len := word len
            FI
        FI
    OD;

    longest word len
);

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

INT longest word len := longest word length(s);
print((whole(longest word len, 0), newline))

```

{% endraw %}

Longest Word in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
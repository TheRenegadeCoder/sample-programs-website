---
authors:
- rzuckerm
date: 2023-01-24
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-01-31
layout: default
tags:
- algol68
- remove-all-whitespace
title: Remove All Whitespace in Algol68
---

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string"));

PROC remove all whitespace := (STRING s) STRING:
(
    STRING t;
    FOR n TO UPB s
    DO
        IF NOT isspace(s[n])
        THEN
            t +:= s[n]
        FI
    OD;

    t
);

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

# Remove all whitespace and display result #
s := remove all whitespace(s);
printf(($gl$, s))

```

{% endraw %}

Remove All Whitespace in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
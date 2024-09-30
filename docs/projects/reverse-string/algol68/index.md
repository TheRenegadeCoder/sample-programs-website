---
authors:
- rzuckerm
date: 2023-01-24
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-03-19
layout: default
tags:
- algol68
- reverse-string
title: Reverse String in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/algol68/how-to-implement-the-solution.md
- sources/programs/reverse-string/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC reverse string = (STRING s) STRING:
(
    STRING t;
    FOR n FROM UPB s DOWNTO 1
    DO
        t +:= s[n]
    OD;

    t
);

# Get 1st command-line argument #
STRING s := argv(4);

# Reverse string and show result #
s := reverse string(s);
printf(($gl$, s))

```

{% endraw %}

Reverse String in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
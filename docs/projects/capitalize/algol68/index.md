---
authors:
- rzuckerm
date: 2023-01-22
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-02-01
layout: default
tags:
- algol68
- capitalize
title: Capitalize in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/algol68/how-to-implement-the-solution.md
- sources/programs/capitalize/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string"));

PROC capitalize = (STRING s) STRING:
(
    # Capitalize first letter if lowercase #
    toupper(s[1]) + s[2:]
);

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

# Capitalize string and show it #
s := capitalize(s);
printf(($gl$, s))

```

{% endraw %}

Capitalize in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
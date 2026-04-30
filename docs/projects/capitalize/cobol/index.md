---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-30
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- capitalize
- cobol
title: Capitalize in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/cobol/how-to-implement-the-solution.md
- sources/programs/capitalize/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. capitalize.

data division.
working-storage section.

01 arg-count        pic 9(4) comp.
01 input-text       pic x(4096).
01 c                pic x.
01 tmp-ord          pic 9(4) comp.

procedure division.

main.
    accept arg-count from argument-number

    if arg-count < 1
        perform show-usage
    end-if

    accept input-text from argument-value

    if input-text = spaces
        perform show-usage
    end-if

    move input-text(1:1) to c

    if c >= "a" and c <= "z"
        compute tmp-ord = function ord(c) - 32
        move function char(tmp-ord) to c
        move c to input-text(1:1)
    end-if

    display function trim(input-text)
    goback.

show-usage.
    display "Usage: please provide a string"
    stop run.

```

{% endraw %}

Capitalize in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
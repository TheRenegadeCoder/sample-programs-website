---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- reverse-string
title: Reverse String in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/cobol/how-to-implement-the-solution.md
- sources/programs/reverse-string/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. reverse-string.

data division.
working-storage section.
01  arg-count           pic 9(4) comp.
01  input-string        pic x(500).

procedure division.
main.
    accept arg-count from argument-number
    if arg-count = 0
        stop run
    end-if

    accept input-string from argument-value
    
    if input-string = spaces
        stop run
    end-if

    display function reverse(input-string)
    
    goback.

```

{% endraw %}

Reverse String in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
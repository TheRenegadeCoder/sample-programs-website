---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: rot13-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- rot13
title: Rot13 in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/cobol/how-to-implement-the-solution.md
- sources/programs/rot13/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. rot13.

data division.
working-storage section.

01 arg-count        pic 9(4) comp.
01 input-text       pic x(500).

01 translation-keys.
    05 alpha-lower   pic x(26) value "abcdefghijklmnopqrstuvwxyz".
    05 rot13-lower   pic x(26) value "nopqrstuvwxyzabcdefghijklm".
    05 alpha-upper   pic x(26) value "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
    05 rot13-upper   pic x(26) value "NOPQRSTUVWXYZABCDEFGHIJKLM".

procedure division.

main.
    accept arg-count from argument-number
    
    if arg-count = 0
        perform show-usage
    end-if

    accept input-text from argument-value
    
    if input-text = spaces
        perform show-usage
    end-if

    perform do-rot13
    goback.

do-rot13.
    inspect input-text 
        converting alpha-lower to rot13-lower
    
    inspect input-text 
        converting alpha-upper to rot13-upper
    
    display function trim(input-text).

show-usage.
    display "Usage: please provide a string to encrypt"
    stop run.

```

{% endraw %}

Rot13 in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
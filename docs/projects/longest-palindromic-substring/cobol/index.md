---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-05
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- cobol
- longest-palindromic-substring
title: Longest Palindromic Substring in COBOL
title1: Longest Palindromic
title2: Substring in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/cobol/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. longest-palindromic-substring.

data division.
working-storage section.

01 ws-s              pic x(200).
01 ws-len            pic 9(4).

01 ws-i              pic 9(4).
01 ws-l              pic 9(4).
01 ws-r              pic 9(4).

01 ws-best-l         pic 9(4) value 0.
01 ws-best-r         pic 9(4) value 0.
01 ws-best-len       pic 9(4) value 0.
01 ws-r-len          pic 9(4) value 0.

01 ws-valid          pic x value "y".
   88 is-valid       value "y".
   88 is-invalid      value "n".

procedure division.

main.
    accept ws-s from argument-value

    if ws-s = spaces
        perform show-usage
        stop run
    end-if

    move function length(function trim(ws-s)) to ws-len

    if ws-len = 0
        perform show-usage
        stop run
    end-if

    perform find-palindrome

    if ws-best-len < 2
        perform show-usage
        stop run
    end-if

    perform varying ws-i from ws-best-l by 1 until ws-i > ws-best-r
        display ws-s(ws-i:1) with no advancing
    end-perform
    stop run.

find-palindrome.
    perform varying ws-i from 1 by 1 until ws-i > ws-len

        move ws-i to ws-l
        move ws-i to ws-r

        perform expand

        move ws-i to ws-l
        compute ws-r = ws-i + 1

        perform expand

    end-perform.

expand.
    perform until ws-l < 1 or ws-r > ws-len
        if ws-s(ws-l:1) not = ws-s(ws-r:1)
            exit perform
        end-if

        compute ws-l = ws-l - 1
        compute ws-r = ws-r + 1
    end-perform

    compute ws-l = ws-l + 1
    compute ws-r = ws-r - 1

    compute ws-r-len = ws-r - ws-l + 1

    if ws-r-len > ws-best-len
        move ws-r-len to ws-best-len
        move ws-l to ws-best-l
        move ws-r to ws-best-r
    end-if.

show-usage.
    display "Usage: please provide a string that contains at least one palindrome".

```

{% endraw %}

Longest Palindromic Substring in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
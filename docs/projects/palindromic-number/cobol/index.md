---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- palindromic-number
title: Palindromic Number in COBOL
title1: Palindromic
title2: Number in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/cobol/how-to-implement-the-solution.md
- sources/programs/palindromic-number/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. palindromic-number.

data division.
working-storage section.
01 cmdargs            pic x(38).

01 buffer-num-area.
    05 buffer-num     pic 9(15).

01 num                pic s9(15) comp.
01 temp               pic s9(15) comp.
01 rev                pic s9(15) comp value 0.
01 digit              pic 9.
01 original           pic s9(15) comp.

procedure division.
main.
    accept cmdargs from command-line

    if cmdargs = spaces or function trim(cmdargs) is not numeric
        perform show-usage
    end-if

    move function trim(cmdargs) to buffer-num
    move buffer-num to num

    if num < 0
        perform show-usage
    end-if

    move num to original
    move num to temp

    perform until temp = 0
        divide temp by 10 giving temp remainder digit
        compute rev = (rev * 10) + digit
    end-perform

    if rev = original
        display "true"
    else
        display "false"
    end-if

    stop run.

show-usage.
    display "Usage: please input a non-negative integer"
    stop run.
```

{% endraw %}

Palindromic Number in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
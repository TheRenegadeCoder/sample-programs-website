---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-05
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- cobol
- fibonacci
title: Fibonacci in COBOL
title1: Fibonacci
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/cobol/how-to-implement-the-solution.md
- sources/programs/fibonacci/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. fibonacci.

data division.
working-storage section.
01 ws-arg        pic x(100).
01 ws-n          pic 9(9) value 0.
01 ws-i          pic 9(9) value 0.

01 ws-i-disp     pic z(9).
01 ws-f-disp     pic z(18).

01 ws-f1         pic 9(18) value 1.
01 ws-f2         pic 9(18) value 1.
01 ws-fnext      pic 9(18) value 0.

procedure division.
main.
    accept ws-arg from command-line

    if ws-arg = spaces
        perform show-usage
        stop run
    end-if

    move function numval(ws-arg) to ws-n

    if ws-n = 0 and function trim(ws-arg) not = "0"
        perform show-usage
        stop run
    end-if

    if ws-n = 0
        stop run
    end-if

    display "1: 1"
    if ws-n = 1
        stop run
    end-if

    display "2: 1"

    perform varying ws-i from 3 by 1 until ws-i > ws-n
        compute ws-fnext = ws-f1 + ws-f2

        move ws-i     to ws-i-disp
        move ws-fnext to ws-f-disp

        display function trim(ws-i-disp) ": "
                function trim(ws-f-disp)

        move ws-f2    to ws-f1
        move ws-fnext to ws-f2
    end-perform

    stop run.

show-usage.
    display "Usage: please input the count of fibonacci numbers to output".
```

{% endraw %}

Fibonacci in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
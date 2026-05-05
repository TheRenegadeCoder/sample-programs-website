---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-05
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- cobol
- maximum-array-rotation
title: Maximum Array Rotation in COBOL
title1: Maximum Array
title2: Rotation in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/cobol/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. maximum-array-rotation.

data division.
working-storage section.

01 ws-input         pic x(200).
01 ws-temp          pic x(200).
01 ws-pos           pic 9(4) value 1.

01 ws-n             pic 9(4) value 0.
01 ws-i             pic 9(4).
01 ws-j             pic 9(4).
01 ws-k             pic 9(4).

01 ws-max-sum       pic s9(18) value 0.
01 ws-sum           pic s9(18) value 0.

01 ws-arr occurs 50 times pic s9(9).
01 ws-rotated occurs 50 times pic s9(9).

01 ws-num           pic s9(9).

01 ws-out           pic -(9)9.

01 ws-valid         pic x value "y".
   88 is-valid      value "y".
   88 is-invalid    value "n".

procedure division.
main.
    accept ws-input from argument-value

    if ws-input = spaces
        perform show-usage
        stop run
    end-if

    perform parse-input

    if is-invalid
        perform show-usage
        stop run
    end-if

    perform compute-maximum-rotation

    move ws-max-sum to ws-out
    display function trim(ws-out)
    stop run.

parse-input.
    set is-valid to true
    move 0 to ws-n
    move 1 to ws-pos
    move ws-input to ws-temp

    perform until ws-pos > function length(function trim(ws-temp))

        unstring ws-temp
            delimited by ","
            into ws-num
            with pointer ws-pos
        end-unstring

        add 1 to ws-n
        move ws-num to ws-arr(ws-n)

    end-perform

    if ws-n = 0
        set is-invalid to true
    end-if.

compute-maximum-rotation.
    move 0 to ws-max-sum

    perform varying ws-k from 0 by 1 until ws-k >= ws-n

        move 0 to ws-sum

        perform varying ws-i from 1 by 1 until ws-i > ws-n

            compute ws-j = ws-i + ws-k
            if ws-j > ws-n
                compute ws-j = ws-j - ws-n
            end-if

            compute ws-sum = ws-sum + ws-arr(ws-j) * (ws-i - 1)

        end-perform

        if ws-sum > ws-max-sum
            move ws-sum to ws-max-sum
        end-if

    end-perform.

show-usage.
    display 'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")'.
```

{% endraw %}

Maximum Array Rotation in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- transpose-matrix
title: Transpose Matrix in COBOL
title1: Transpose
title2: Matrix in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/cobol/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. transpose-matrix.

data division.
working-storage section.

01 cmd-args.
    05 cols-raw    pic x(8).
    05 rows-raw    pic x(8).
    05 matrix-raw      pic x(500).

01 matrix-dims.
    05 num-cols          pic 9(4) comp.
    05 num-rows            pic 9(4) comp.
    05 total-elements  pic 9(4) comp.

01 table-indices.
    05 i               pic s9(4) comp.
    05 j               pic s9(4) comp.
    05 curr-pos        pic 9(4) comp value 1.
    05 element-ptr     pic 9(4) comp value 1.

01 matrix-data.
    05 row occurs 100 times.
        10 val occurs 100 times
            pic 9(9) comp.

01 output-utils.
    05 display-num     pic z(8)9.
    05 is-first pic x value "Y".
        88 first-item value "Y".
        88 not-first  value "N".

procedure division.

main-logic.
    perform get-and-validate-input
    perform parse-matrix
    perform print-transposed
    display space
    goback.

get-and-validate-input.
    accept cols-raw from argument-value
    accept rows-raw from argument-value
    accept matrix-raw from argument-value

    if cols-raw = spaces or rows-raw = spaces or matrix-raw = spaces
        or function trim(cols-raw) is not numeric
        or function trim(rows-raw) is not numeric
        display "Usage: please enter the dimension of the matrix and the serialized matrix"
        stop run
    end-if

    compute num-cols = function numval(cols-raw)
    compute num-rows = function numval(rows-raw)
    compute total-elements = num-cols * num-rows.

parse-matrix.
    move 1 to i
    move 1 to j
    move 1 to curr-pos

    perform until i > num-rows

        unstring matrix-raw
            delimited by ", "
            into val(i, j)
            pointer curr-pos
        end-unstring

        add 1 to j

        if j > num-cols
            move 1 to j
            add 1 to i
        end-if

    end-perform.

print-transposed.
    set first-item to true

    perform varying j from 1 by 1 until j > num-cols
        perform varying i from 1 by 1 until i > num-rows
            
            if not-first
                display ", " with no advancing
            end-if

            move val(i, j) to display-num
            display function trim(display-num) with no advancing
            
            set not-first to true
        end-perform
    end-perform.

```

{% endraw %}

Transpose Matrix in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
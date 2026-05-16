---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-01
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-05-01
layout: default
tags:
- cobol
- convex-hull
title: Convex Hull in COBOL
title1: Convex Hull
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/cobol/how-to-implement-the-solution.md
- sources/programs/convex-hull/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. convex-hull.

data division.
working-storage section.

01  arg-processing.
    05  arg-count           pic 9(4) comp-5.
    05  arg-x               pic x(4096).
    05  arg-y               pic x(4096).
    05  arg-len             pic 9(4) comp-5.

01  point-cloud.
    05  n                   pic 9(4) comp-5 value 0.
    05  points occurs 100 times indexed by pt-idx, inner-idx, k-idx.
        10  pt-x            pic s9(9) comp-5.
        10  pt-y            pic s9(9) comp-5.

01  hull-logic.
    05  k                   pic 9(4) comp-5 value 0.
    05  hull-indices occurs 200 times pic 9(4) comp-5.
    05  min-k               pic 9(4) comp-5.
    05  start-idx           pic s9(4) comp-5.
    05  cross-product       pic s9(18) comp-5.
        88  is-strictly-clockwise value -999999999999999999 thru -1.

01  parsing-helpers.
    05  delim               pic x value ",".
    05  ptr                 pic 9(4) comp-5.
    05  val-str             pic x(20).
    05  temp-x              pic s9(9) comp-5.
    05  temp-y              pic s9(9) comp-5.
    05  char-idx            pic 9(4) comp-5.

01  display-format.
    05  out-x               pic -(9)9.
    05  out-y               pic -(9)9.
    05  out-line            pic x(50).

procedure division.

main.
    accept arg-count from argument-number
    if arg-count < 2
        perform show-usage
    end-if

    accept arg-x from argument-value
    accept arg-y from argument-value

    perform parse-input

    if n < 3
        perform show-usage
    end-if

    perform sort-points
    perform build-convex-hull
    perform display-results
    goback.

parse-input.
    move 1 to ptr
    compute arg-len = function length(function trim(arg-x))
    perform varying n from 1 by 1 until ptr > arg-len
        move spaces to val-str
        unstring arg-x delimited by delim into val-str pointer ptr
        if val-str = spaces 
            exit perform 
        end-if
        perform validate-val-str
        compute pt-x(n) = function numval(val-str)
    end-perform
    compute n = n - 1

    move 1 to ptr
    compute arg-len = function length(function trim(arg-y))
    perform varying inner-idx from 1 by 1 until inner-idx > n
        if ptr > arg-len 
            perform show-usage 
        end-if
        move spaces to val-str
        unstring arg-y delimited by delim into val-str pointer ptr
        if val-str = spaces 
            perform show-usage 
        end-if
        perform validate-val-str
        compute pt-y(inner-idx) = function numval(val-str)
    end-perform

    move spaces to val-str
    unstring arg-y delimited by delim into val-str pointer ptr
    if val-str not = spaces 
        perform show-usage 
    end-if.

validate-val-str.
    perform varying char-idx from 1 by 1 until
        char-idx > function length(function trim(val-str))
        if val-str(char-idx:1) not numeric and
            val-str(char-idx:1) not = "-" and
            val-str(char-idx:1) not = " "
            perform show-usage
        end-if
    end-perform.

sort-points.
    perform varying pt-idx from 1 by 1 until pt-idx > n - 1
        perform varying inner-idx from 1 by 1 until
            inner-idx > n - pt-idx
            compute k-idx = inner-idx + 1
            if pt-x(inner-idx) > pt-x(k-idx) or
                (pt-x(inner-idx) = pt-x(k-idx) and
                pt-y(inner-idx) > pt-y(k-idx))
                move pt-x(inner-idx) to temp-x
                move pt-y(inner-idx) to temp-y
                move pt-x(k-idx) to pt-x(inner-idx)
                move pt-y(k-idx) to pt-y(inner-idx)
                move temp-x to pt-x(k-idx)
                move temp-y to pt-y(k-idx)
            end-if
        end-perform
    end-perform.

build-convex-hull.
    move 0 to k

    perform varying pt-idx from 1 by 1 until pt-idx > n
        perform pop-back-points
        add 1 to k
        move pt-idx to hull-indices(k)
    end-perform

    compute min-k = k + 1
    compute start-idx = n - 1
    perform varying pt-idx from start-idx by -1 until pt-idx < 1
        perform pop-back-points
        add 1 to k
        move pt-idx to hull-indices(k)
    end-perform
    subtract 1 from k.

pop-back-points.
    perform until k < 2
        perform calculate-cross-product
        if is-strictly-clockwise
            subtract 1 from k
        else
            exit perform
        end-if
    end-perform.

calculate-cross-product.
    compute cross-product =
        (pt-x(hull-indices(k)) - pt-x(hull-indices(k - 1))) *
        (pt-y(pt-idx) - pt-y(hull-indices(k - 1))) -
        (pt-y(hull-indices(k)) - pt-y(hull-indices(k - 1))) *
        (pt-x(pt-idx) - pt-x(hull-indices(k - 1))).

display-results.
    perform varying pt-idx from 1 by 1 until pt-idx > k
        move pt-x(hull-indices(pt-idx)) to out-x
        move pt-y(hull-indices(pt-idx)) to out-y
        string "(" function trim(out-x) ", "
                function trim(out-y) ")"
                delimited by size into out-line
        display function trim(out-line)
        move spaces to out-line
    end-perform.

show-usage.
    display "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. ""100, 440, 210"")"
    stop run.

```

{% endraw %}

Convex Hull in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
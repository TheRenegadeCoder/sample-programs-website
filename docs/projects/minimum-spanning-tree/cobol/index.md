---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- minimum-spanning-tree
title: Minimum Spanning Tree in COBOL
title1: Minimum Spanning
title2: Tree in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/cobol/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. minimum-spanning-tree.

data division.
working-storage section.
01 input-str            pic x(4000).

01 matrix-area.
    05 matrix-row        occurs 25 times 
                         indexed by row-idx.
        10 adj-val       occurs 25 times 
                         indexed by col-idx 
                         pic 9(9) comp-5.

01 state.
    05 node-count        pic 9(4) comp-5.
    05 total-elements    pic 9(4) comp-5.
    05 mst-weight        pic 9(15) comp-5 value 0.
    05 infinity          pic 9(9) comp-5 value 999999999.
    05 current-token     pic x(15).

01 work-tables.
    05 visited-flg       occurs 25 times 
                         indexed by v-idx 
                         pic x value 'n'.
        88 is-visited     value 'y'.
        88 is-not-visited value 'n'.
    05 min-dist          occurs 25 times 
                         indexed by d-idx 
                         pic 9(9) comp-5.

01 counters.
    05 u                 pic 9(4) comp-5.
    05 v                 pic 9(4) comp-5.
    05 ptr               pic 9(4) comp-5.
    05 min-val           pic 9(9) comp-5.

01 display-area.
    05 result-out        pic z(14)9.

procedure division.
main.
    accept input-str from argument-value
    if input-str = spaces perform show-usage end-if

    perform parse-and-validate
    perform find-mst
    
    move mst-weight to result-out
    display function trim(result-out)
    stop run.

parse-and-validate.
    move 0 to total-elements
    inspect function trim(input-str) tallying total-elements for all ","
    add 1 to total-elements

    compute node-count = function integer(function sqrt(total-elements))
    if (node-count * node-count not = total-elements) 
        or total-elements > 625
        perform show-usage
    end-if

    move 1 to ptr
    perform varying row-idx from 1 by 1 until row-idx > node-count
        perform varying col-idx from 1 by 1 until col-idx > node-count
            unstring input-str delimited by ","
                into current-token
                pointer ptr
            compute adj-val(row-idx, col-idx) = function numval(current-token)
        end-perform
    end-perform.

find-mst.
    perform varying d-idx from 1 by 1 until d-idx > node-count
        move infinity to min-dist(d-idx)
        set is-not-visited(d-idx) to true
    end-perform

    move 0 to min-dist(1)

    perform node-count times
        move infinity to min-val
        move 0 to u
        
        perform varying v-idx from 1 by 1 until v-idx > node-count
            if is-not-visited(v-idx) and min-dist(v-idx) < min-val
                move min-dist(v-idx) to min-val
                set v to v-idx
                move v to u
            end-if
        end-perform

        if u = 0 exit perform end-if

        set is-visited(u) to true
        add min-dist(u) to mst-weight
        
        perform varying v from 1 by 1 until v > node-count
            if is-not-visited(v) 
                and adj-val(u, v) > 0
                and adj-val(u, v) < min-dist(v)
                move adj-val(u, v) to min-dist(v)
            end-if
        end-perform
    end-perform.

show-usage.
    display "Usage: please provide a comma-separated list of integers"
    stop run.

```

{% endraw %}

Minimum Spanning Tree in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
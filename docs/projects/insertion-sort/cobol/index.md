---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-21
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2026-04-21
layout: default
tags:
- cobol
- insertion-sort
title: Insertion Sort in COBOL
title1: Insertion
title2: Sort in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/cobol/how-to-implement-the-solution.md
- sources/programs/insertion-sort/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. insertion-sort.

data division.
working-storage section.

01 max-entries          constant as 1000.

01 argument-string      pic x(32768).
01 current-token        pic x(128).
01 scan-ptr             binary-long.

01 sort-table.
    05 list-size        binary-long value 0.
    05 entry-value      pic s9(9) occurs 0 to max-entries 
                        depending on list-size.

01 work-vars.
    05 i                binary-long.
    05 j                binary-long.
    05 key-val          pic s9(9).

01 flags.
    05 swap-flag        pic x.
        88 has-swapped  value 'Y'.
        88 no-swaps     value 'N'.

01 output-formatting.
    05 display-num      pic ---------9.
    05 separator        pic x(2) value ", ".

procedure division.

main.
    perform validate-input
    perform parse-input
    perform execute-sort
    perform display-results
    goback.

validate-input.
    accept argument-string from argument-value
    if argument-string = spaces
        perform show-usage
    end-if.

parse-input.
    move 1 to scan-ptr
    
    perform until scan-ptr > length of argument-string
        move spaces to current-token
        
        unstring argument-string delimited by ","
            into current-token with pointer scan-ptr
        end-unstring

        if current-token = spaces
            continue
        end-if

        if function test-numval(function trim(current-token)) <> 0
            perform show-usage
        end-if

        add 1 to list-size
        if list-size > max-entries
            perform show-usage
        end-if
        
        move function numval(current-token) to entry-value(list-size)
    end-perform

    if list-size < 2 perform show-usage end-if.

execute-sort.
    perform varying i from 2 by 1 until i > list-size
        move entry-value(i) to key-val
        move i to j

        perform until j <= 1 or entry-value(j - 1) <= key-val
            move entry-value(j - 1) to entry-value(j)
            subtract 1 from j
        end-perform

        move key-val to entry-value(j)
    end-perform.

display-results.
    perform varying i from 1 by 1 until i > list-size
        if i > 1
            display separator with no advancing
        end-if
        
        move entry-value(i) to display-num
        display function trim(display-num) with no advancing
    end-perform
    display space.

show-usage.
    display
        'Usage: please provide a list of at least two integers '
        'to sort in the format "1, 2, 3, 4, 5"'
    stop run.

```

{% endraw %}

Insertion Sort in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
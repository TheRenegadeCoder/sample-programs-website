---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-21
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-04-21
layout: default
tags:
- cobol
- quick-sort
title: Quick Sort in COBOL
title1: Quick Sort
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/cobol/how-to-implement-the-solution.md
- sources/programs/quick-sort/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. quick-sort.

data division.
working-storage section.

78 max-entries value 1000.
78 stack-size  value 64.

01 argument-string  pic x(32768).
01 token            pic x(32).
01 scan-ptr         binary-long value 1.
01 list-size        binary-long value 0.

01 array-a.
   05 item occurs 1 to max-entries
      depending on list-size
      pic s9(9).

01 stack.
   05 stack-ptr binary-long value 0.
   05 frame occurs stack-size.
      10 low-bound  binary-long.
      10 high-bound binary-long.

01 low     binary-long.
01 high    binary-long.
01 mid     binary-long.
01 i       binary-long.
01 j       binary-long.

01 pivot   pic s9(9).
01 temp    pic s9(9).
01 out-num pic -(10)9.

procedure division.

main.
    perform initialize-program
    perform read-input

    if list-size < 2
        perform display-usage
    else
        perform quicksort
    end-if

    perform display-results
    stop run.

*> -------------------------
initialize-program.
    move 1 to scan-ptr
    move 0 to list-size.

*> -------------------------
read-input.
    accept argument-string from argument-value

    if function trim(argument-string) = spaces
        perform display-usage
    end-if

    perform tokenize.

tokenize.
    perform until scan-ptr > length of argument-string
        move spaces to token
        
        unstring argument-string
            delimited by ","
            into token
            with pointer scan-ptr
        end-unstring

        if function trim(token) not = spaces
            if function test-numval(token) not = 0
                perform display-usage
            end-if

            add 1 to list-size
            if list-size > max-entries
                perform display-usage
            end-if

            move function numval(token) to item(list-size)
        end-if
    end-perform.

*> -------------------------
quicksort.
    move 1 to stack-ptr
    move 1 to low-bound(1)
    move list-size to high-bound(1)

    perform until stack-ptr = 0

        move low-bound(stack-ptr) to low
        move high-bound(stack-ptr) to high
        subtract 1 from stack-ptr

        perform until low >= high

            *> -------- pivot (median of 3) --------
            compute mid = low + (high - low) / 2

            if item(low) > item(mid)
                move item(low) to temp
                move item(mid) to item(low)
                move temp to item(mid)
            end-if

            if item(low) > item(high)
                move item(low) to temp
                move item(high) to item(low)
                move temp to item(high)
            end-if

            if item(mid) > item(high)
                move item(mid) to temp
                move item(high) to item(mid)
                move temp to item(high)
            end-if

            move item(mid) to pivot

            *> -------- partition --------
            move low to i
            move high to j

            perform until i > j

                perform until i > high or item(i) >= pivot
                    add 1 to i
                end-perform

                perform until j < low or item(j) <= pivot
                    subtract 1 from j
                end-perform

                if i <= j
                    move item(i) to temp
                    move item(j) to item(i)
                    move temp to item(j)
                    add 1 to i
                    subtract 1 from j
                end-if

            end-perform

            *> -------- stack management --------
            if (j - low) < (high - i)

                if i < high and stack-ptr < stack-size
                    add 1 to stack-ptr
                    move i to low-bound(stack-ptr)
                    move high to high-bound(stack-ptr)
                end-if

                move j to high

            else

                if low < j and stack-ptr < stack-size
                    add 1 to stack-ptr
                    move low to low-bound(stack-ptr)
                    move j to high-bound(stack-ptr)
                end-if

                move i to low

            end-if

        end-perform

    end-perform.

*> -------------------------
display-results.
    perform varying i from 1 by 1 until i > list-size
        move item(i) to out-num
        display function trim(out-num) with no advancing

        if i < list-size
            display ", " with no advancing
        end-if
    end-perform

    display space.

*> -------------------------
display-usage.
    display 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'
    stop run.

```

{% endraw %}

Quick Sort in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
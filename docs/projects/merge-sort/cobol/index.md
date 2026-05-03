---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-21
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-04-21
layout: default
tags:
- cobol
- merge-sort
title: Merge Sort in COBOL
title1: Merge Sort
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/cobol/how-to-implement-the-solution.md
- sources/programs/merge-sort/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. merge-sort.

data division.
working-storage section.
01 max-entries      constant as 1000.

01 argument-string  pic x(32768).
01 current-token    pic x(128).
01 scan-ptr         binary-long.

01 table-a.
    05 list-size    binary-long value 0.
    05 array-a      pic s9(9) occurs max-entries.
01 table-b.
    05 array-b      pic s9(9) occurs max-entries.

01 sort-state.
    05 merge-size   binary-long.
    05 left-idx     binary-long.
    05 mid-idx      binary-long.
    05 right-idx    binary-long.
    05 pass-count   binary-long.
    05 left-ptr     binary-long.
    05 right-ptr    binary-long.
    05 target-ptr   binary-long.
    05 i            binary-long.

01 output-fmt.
    05 display-num  pic -(10)9.
    05 comma-space  pic xx value ", ".

procedure division.

main.
    perform get-input
    perform parse-input
    perform execute-sort
    perform display-results
    goback.

get-input.
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
        
        if current-token = spaces continue end-if
        if function test-numval(function trim(current-token)) <> 0
            perform show-usage
        end-if

        add 1 to list-size
        if list-size > max-entries perform show-usage end-if
        move function numval(current-token) to array-a(list-size)
    end-perform
    if list-size < 2 perform show-usage end-if.

execute-sort.
    move 1 to merge-size
    move 0 to pass-count
    
    perform until merge-size >= list-size
        move 1 to left-idx
        perform until left-idx > list-size
            compute mid-idx = left-idx + merge-size - 1
            compute right-idx = 
                function min(left-idx + 2 * merge-size - 1, list-size)
            
            if mid-idx < list-size
                if function mod(pass-count, 2) = 0
                    perform merge-a-to-b
                else
                    perform merge-b-to-a
                end-if
            else
                perform copy-leftover
            end-if
            
            compute left-idx = left-idx + 2 * merge-size
        end-perform
        
        compute merge-size = merge-size * 2
        add 1 to pass-count
    end-perform.

merge-a-to-b.
    move left-idx to left-ptr
    compute right-ptr = mid-idx + 1
    move left-idx to target-ptr

    perform until left-ptr > mid-idx or right-ptr > right-idx
        if array-a(left-ptr) <= array-a(right-ptr)
            move array-a(left-ptr) to array-b(target-ptr)
            add 1 to left-ptr
        else
            move array-a(right-ptr) to array-b(target-ptr)
            add 1 to right-ptr
        end-if
        add 1 to target-ptr
    end-perform

    perform until left-ptr > mid-idx
        move array-a(left-ptr) to array-b(target-ptr)
        add 1 to left-ptr add 1 to target-ptr
    end-perform

    perform until right-ptr > right-idx
        move array-a(right-ptr) to array-b(target-ptr)
        add 1 to right-ptr add 1 to target-ptr
    end-perform.

merge-b-to-a.
    move left-idx to left-ptr
    compute right-ptr = mid-idx + 1
    move left-idx to target-ptr

    perform until left-ptr > mid-idx or right-ptr > right-idx
        if array-b(left-ptr) <= array-b(right-ptr)
            move array-b(left-ptr) to array-a(target-ptr)
            add 1 to left-ptr
        else
            move array-b(right-ptr) to array-a(target-ptr)
            add 1 to right-ptr
        end-if

        add 1 to target-ptr
    end-perform

    perform until left-ptr > mid-idx
        move array-b(left-ptr) to array-a(target-ptr)
        add 1 to left-ptr add 1 to target-ptr
    end-perform

    perform until right-ptr > right-idx
        move array-b(right-ptr) to array-a(target-ptr)
        add 1 to right-ptr add 1 to target-ptr
    end-perform.

copy-leftover.
    perform varying i from left-idx by 1 until i > right-idx
        if function mod(pass-count, 2) = 0
            move array-a(i) to array-b(i)
        else
            move array-b(i) to array-a(i)
        end-if
    end-perform.

display-results.
    perform varying i from 1 by 1 until i > list-size
        if function mod(pass-count, 2) = 0
            move array-a(i) to display-num
        else
            move array-b(i) to display-num
        end-if
        
        display function trim(display-num) with no advancing
        if i < list-size
            display ", " with no advancing
        end-if
    end-perform
    
    display space.

show-usage.
    display
        'Usage: please provide a list of at least two integers '
        'to sort in the format "1, 2, 3, 4, 5"'
    stop run.

```

{% endraw %}

Merge Sort in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
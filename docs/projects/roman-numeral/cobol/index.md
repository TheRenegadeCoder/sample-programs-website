---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- cobol
- roman-numeral
title: Roman Numeral in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/cobol/how-to-implement-the-solution.md
- sources/programs/roman-numeral/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. roman-numeral.

data division.
working-storage section.
01  arg-count           pic 9(4) comp.
01  roman-input         pic x(100).
01  input-len           pic 9(4) comp.
01  total-decimal       pic 9(9) comp value 0.

01 roman-map-area pic x(35)
    value "M1000D0500C0100L0050X0010V0005I0001".

01 roman-table redefines roman-map-area
    occurs 7 times indexed by r-idx.
    05 r-char pic x.
    05 r-val  pic 9(4).

01  i                   pic 9(4) comp.
01  current-n           pic 9(4) comp.
01  next-n              pic 9(4) comp.
01  search-char         pic x.
01  search-result       pic 9(4) comp.
01  display-num         pic z(8)9. 

procedure division.
main.
    accept arg-count from argument-number
    if arg-count = 0
        display "Usage: please provide a string of roman numerals"
        stop run
    end-if

    accept roman-input from argument-value
    if roman-input = spaces
        display "0" stop run
    end-if

    compute input-len = function length(function trim(roman-input))

    perform varying i from 1 by 1 until i > input-len
        
        *> Get current value
        move roman-input(i:1) to search-char
        perform find-val
        move search-result to current-n
        
        if current-n = 0
            display "Error: invalid string of roman numerals" stop run
        end-if

        *> Peek at next value
        if i < input-len
            move roman-input(i + 1:1) to search-char
            perform find-val
            move search-result to next-n
        else
            move 0 to next-n
        end-if

        if current-n < next-n
            subtract current-n from total-decimal
        else
            add current-n to total-decimal
        end-if
    end-perform

    move total-decimal to display-num
    display function trim(display-num) 
    goback.

find-val.
    move 0 to search-result

    perform varying r-idx from 1 by 1 until r-idx > 7
        if r-char(r-idx) = search-char
            move r-val(r-idx) to search-result
            exit perform
        end-if
    end-perform.

```

{% endraw %}

Roman Numeral in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
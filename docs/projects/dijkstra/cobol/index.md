---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-01
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-01
layout: default
tags:
- cobol
- dijkstra
title: Dijkstra in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/cobol/how-to-implement-the-solution.md
- sources/programs/dijkstra/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. dijkstra.

data division.
working-storage section.

01 matrix-input        pic x(5000).
01 source-input        pic x(16).
01 dest-input          pic x(16).

01 usage-msg pic x(200)
    value 'Usage: please provide three inputs: a serialized matrix, a source node and a destination node'.

01 n                  pic 9(4) comp.
01 i                  pic 9(4) comp.
01 j                  pic 9(4) comp.

01 src                pic 9(4) comp.
01 dst                pic 9(4) comp.

01 cnt                pic 9(4) comp.
01 ptr                pic 9(4) comp.
01 token              pic x(32).

01 min-dist           pic 9(9) comp.
01 min-index          pic 9(4) comp.

01 cell-values        pic 9(9) comp occurs 10000 times.

01 visited.
   05 vis pic 9 comp occurs 100 times.

01 dist.
   05 d pic 9(9) comp occurs 100 times.

01 matrix.
   05 matrix-cell pic 9(9) comp occurs 10000 times.

01 out-num pic z(9)9.

procedure division.

main.
    accept matrix-input from argument-value
    accept source-input from argument-value
    accept dest-input from argument-value

    if matrix-input = spaces
       or source-input = spaces
       or dest-input = spaces
        perform show-usage
    end-if

    if source-input(1:1) = "-" and function length(function trim(source-input)) > 1
        perform show-usage
    end-if

    if dest-input(1:1) = "-" and function length(function trim(dest-input)) > 1
        perform show-usage
    end-if

    move function numval(source-input) to src
    move function numval(dest-input) to dst

    if src < 0 or dst < 0
        perform show-usage
    end-if

    perform parse-matrix

    if n = 0
        perform show-usage
    end-if

    if src >= n or dst >= n
        perform show-usage
    end-if

    perform dijkstra

    if d(dst) = 999999999
        perform show-usage
    end-if

    move d(dst) to out-num
    display function trim(out-num)
    goback.


parse-matrix.
    move 0 to cnt
    move 1 to ptr

    perform until ptr > function length(function trim(matrix-input))

        move spaces to token

        unstring matrix-input
            delimited by ","
            into token
            with pointer ptr
        end-unstring

        if token not = spaces

            if function numval(token) < 0
                perform show-usage
            end-if

            add 1 to cnt
            move function numval(token) to matrix-cell(cnt)
        end-if

    end-perform

    compute n = function integer(function sqrt(cnt))

    if n * n not = cnt
        perform show-usage
    end-if.


dijkstra.
    perform varying i from 0 by 1 until i > n - 1
        move 999999999 to d(i)
        move 0 to vis(i)
    end-perform

    move 0 to d(src)

    perform varying i from 0 by 1 until i > n - 1

        move 999999999 to min-dist
        move -1 to min-index

        perform varying j from 0 by 1 until j > n - 1
            if vis(j) = 0 and d(j) < min-dist
                move d(j) to min-dist
                move j to min-index
            end-if
        end-perform

        if min-index = -1
            exit perform
        end-if

        move 1 to vis(min-index)

        perform varying j from 0 by 1 until j > n - 1

            if vis(j) = 0
               and matrix-cell((min-index * n) + j + 1) > 0
               and d(min-index) not = 999999999

                if d(min-index) + matrix-cell((min-index * n) + j + 1) < d(j)
                    compute d(j) =
                        d(min-index) + matrix-cell((min-index * n) + j + 1)
                end-if
            end-if

        end-perform

    end-perform.


show-usage.
    display usage-msg
    stop run.
```

{% endraw %}

Dijkstra in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
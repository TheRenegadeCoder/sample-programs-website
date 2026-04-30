---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-01
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2026-05-01
layout: default
tags:
- cobol
- depth-first-search
title: Depth First Search in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/cobol/how-to-implement-the-solution.md
- sources/programs/depth-first-search/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. depth-first-search.

data division.
working-storage section.

01 argument-count           pic 9(4) comp.

01 tree-input               pic x(8192).
01 vertex-values-input      pic x(4096).
01 target-value-input       pic x(128).

01 adjacency-matrix.
   05 adjacency-cell pic 9 occurs 10000 times.

01 node-value.
   05 node pic s9(9) comp occurs 100 times.

01 node-stack.
   05 stack-node pic 9(4) comp occurs 100 times.
01 stack-top pic 9(4) comp value 0.

01 visited-nodes.
   05 visited-node pic 9 comp occurs 100 times.

01 node-count          pic 9(4) comp value 0.
01 cell-count          pic 9(4) comp value 0.

01 i                  pic 9(4) comp.
01 j                  pic 9(4) comp.
01 matrix-index       pic 9(4) comp.
01 current-node       pic 9(4) comp.

01 target-node-value  pic s9(9) comp.

procedure division.

main.
    accept argument-count from argument-number

    if argument-count not = 3
        perform show-usage
    end-if

    accept tree-input from argument-value
    accept vertex-values-input from argument-value
    accept target-value-input from argument-value

    if tree-input = spaces
       or vertex-values-input = spaces
       or target-value-input = spaces
        perform show-usage
    end-if

    move function numval(target-value-input) to target-node-value

    perform parse-adjacency-matrix
    perform parse-vertex-values

    if node-count = 0
        perform show-usage
    end-if

    perform depth-first-search

    goback.

parse-adjacency-matrix.
    move 0 to cell-count

    perform varying i from 1 by 1
        until i > function length(function trim(tree-input))

        if tree-input(i:1) >= "0"
           and tree-input(i:1) <= "9"

            add 1 to cell-count
            move function numval(tree-input(i:1))
                to adjacency-cell(cell-count)
        end-if
    end-perform

    compute node-count =
        function integer(function sqrt(cell-count))

    if node-count * node-count not = cell-count
        perform show-usage
    end-if.

parse-vertex-values.
    move 0 to node-count
    move 1 to j

    perform varying i from 1 by 1
        until i > function length(function trim(vertex-values-input))

        if vertex-values-input(i:1) >= "0"
           and vertex-values-input(i:1) <= "9"

            add 1 to node-count
            move function numval(vertex-values-input(i:1))
                to node(node-count)
        end-if
    end-perform.

    if node-count = 0
        perform show-usage
    end-if.

depth-first-search.
    move 1 to stack-top
    move 1 to stack-node(stack-top)

    perform varying i from 1 by 1 until i > node-count
        move 0 to visited-node(i)
    end-perform

    perform until stack-top = 0

        move stack-node(stack-top) to current-node
        subtract 1 from stack-top

        if visited-node(current-node) = 1
            exit perform
        end-if

        move 1 to visited-node(current-node)

        if node(current-node) = target-node-value
            display "true"
            goback
        end-if

        perform varying i from node-count by -1 until i = 0
            compute matrix-index =
                (current-node - 1) * node-count + i

            if adjacency-cell(matrix-index) = 1
               and visited-node(i) = 0

                add 1 to stack-top
                move i to stack-node(stack-top)
            end-if
        end-perform

    end-perform

    display "false"
    goback.

show-usage.
    display 'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")'
    stop run.

```

{% endraw %}

Depth First Search in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
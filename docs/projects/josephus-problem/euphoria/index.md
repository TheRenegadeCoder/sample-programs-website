---
authors:
- rzuckerm
date: 2023-02-25
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2023-02-25
layout: default
tags:
- euphoria
- josephus-problem
title: Josephus Problem in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/euphoria/how-to-implement-the-solution.md
- sources/programs/josephus-problem/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/math.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

procedure usage()
    puts(STDOUT, "Usage: please input the total number of people and number of people to skip.\n")
    abort(0)
end procedure

-- Reference: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
--
-- Use zero-based index algorithm:
--
--    g(1, k) = 0
--    g(m, k) = [g(m - 1, k) + k] MOD m, for m = 2, 3, ..., n
--
-- Final answer is g(n, k) + 1 to get back to one-based index
function josephus(integer n, integer k)
    integer g = 0
    for m = 2 to n
    do
        g = mod(g + k, m)
    end for

    return g + 1
end function

-- Check 1st and 2nd command-line argument
sequence argv = command_line()
if length(argv) < 5 or length(argv[4]) = 0 or length(argv[5]) = 0
then
    usage()
end if

-- Parse 1st and second command-line argument
sequence arg_nums = {4, 5}
sequence values = {}
for m = 1 to 2
do
    sequence result = parse_int(argv[arg_nums[m]])
    values &= result[PARSE_INT_VALUE]
    if not result[PARSE_INT_VALID]
    then
        usage()
    end if
end for

-- Calculate Josephus problem and display
integer n = values[1]
integer k = values[2]
integer g = josephus(n, k)
printf(STDOUT, "%d\n", g)

```

{% endraw %}

Josephus Problem in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2023-02-19
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2023-02-27
layout: default
tags:
- bubble-sort
- euphoria
title: Bubble Sort in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/euphoria/how-to-implement-the-solution.md
- sources/programs/bubble-sort/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e

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

-- Indices for parse_int_list() return value
enum PARSE_INT_LIST_VALID, PARSE_INT_LIST_VALUES

function parse_int_list(sequence s)
    -- Split string on comma
    sequence list = split(s, ",")

    -- Parse each item
    integer valid = FALSE
    sequence values = {}
    for n = 1 to length(list)
    do
        sequence result = parse_int(list[n])
        valid = result[PARSE_INT_VALID]
        values &= result[PARSE_INT_VALUE]
        if not valid
        then
            exit
        end if
    end for

    return {valid, values}
end function

procedure usage()
    puts(
        STDOUT, 
        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n"
    )
    abort(0)
end procedure

procedure show_list_values(sequence values)
    if length(values) > 0
    then
        sequence format = repeat_pattern("%d, ", length(values))
        sequence s = sprintf(format[1..$-2], values)
        printf(STDOUT, "%s\n", {s})
    end if
end procedure

function bubble_sort(sequence values)
    -- Source: https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort

    integer n = length(values)
    integer new_n
    integer temp
    loop
    do
        new_n = 1
        for i = 2 to n
        do
            if values[i - 1] > values[i]
            then
                temp = values[i - 1]
                values[i - 1] = values[i]
                values[i] = temp
                new_n = i
            end if
        end for

        n = new_n
    until n <= 2
    end loop

    return values
end function

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int_list(argv[4])
sequence values = result[PARSE_INT_LIST_VALUES]
if not result[PARSE_INT_LIST_VALID] or length(values) < 2
then
    usage()
end if

-- Do bubble sort and show results
values = bubble_sort(values)
show_list_values(values)

```

{% endraw %}

Bubble Sort in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
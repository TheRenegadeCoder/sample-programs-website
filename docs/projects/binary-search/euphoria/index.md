---
authors:
- rzuckerm
date: 2023-02-19
featured-image: binary-search-in-every-language.jpg
last-modified: 2023-02-19
layout: default
tags:
- binary-search
- euphoria
title: Binary Search in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/euphoria/how-to-implement-the-solution.md
- sources/programs/binary-search/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/search.e
include std/utils.e

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
        "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n"
    )
    abort(0)
end procedure

function check_sorted(sequence values)
    for k = 1 to length(values) - 1
    do
        if values[k] > values[k + 1]
        then
            return FALSE
        end if
    end for

    return TRUE
end function

-- Check command-line arguments
sequence argv = command_line()
if length(argv) < 5 or length(argv[4]) = 0 or length(argv[5]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence list_result = parse_int_list(argv[4])
sequence values = list_result[PARSE_INT_LIST_VALUES]
if not list_result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Parse 2nd command-line argument
sequence result = parse_int(argv[5])
integer target = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID]
then
    usage()
end if

-- Make sure list is sorted
if not check_sorted(values)
then
    usage()
end if

-- Use built-in binary search and show results
integer index = binary_search(target, values)
puts(STDOUT, iif(index > 0, "true\n", "false\n"))

```

{% endraw %}

Binary Search in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
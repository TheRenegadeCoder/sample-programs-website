---
authors:
- rzuckerm
date: 2023-02-27
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2023-02-27
layout: default
tags:
- euphoria
- longest-common-subsequence
title: Longest Common Subsequence in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/euphoria/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
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
    puts(STDOUT, "Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"\n")
    abort(0)
end procedure

-- Longest Common Sequence
-- Source: https://en.wikipedia.org/wiki/Longest_common_subsequence#Example_in_C#
--
-- However, instead of storing lengths, a subsequence index is stored.
-- Subsequences are stored in a separate array. The indices used for the
-- "c" array in the above source are offset by 1 due to the fact that
-- one-based instead of zero-based indexing must be used
function longest_common_subsequence(sequence list1, sequence list2)
    -- Initialize all subsequences to an empty sequence
    integer m = length(list1)
    integer n = length(list2)
    sequence c = repeat(repeat(1, n + 1), m + 1)
    sequence subsequences = {{}}

    -- Find the longest common subsequence using prior subsequences
    integer index1
    integer index2
    for i = 1 to m
    do
        for j = 1 to n
        do
            -- If common element found, create new subsequence based on prior
            -- subsequence with the common element appended
            if list1[i] = list2[j]
            then
                subsequences &= {subsequences[c[i][j]] & list1[i]}
                c[i + 1][j + 1] = length(subsequences)
            -- Else, reuse the longer of the two prior subsequences
            else
                index1 = c[i + 1][j]
                index2 = c[i][j + 1]
                c[i + 1][j + 1] = iif(
                    length(subsequences[index1]) > length(subsequences[index2]),
                    index1,
                    index2
                )
            end if
        end for
    end for

    return subsequences[c[m + 1][n + 1]]
end function

procedure show_list_values(sequence values)
    if length(values) > 0
    then
        sequence format = repeat_pattern("%d, ", length(values))
        sequence s = sprintf(format[1..$-2], values)
        printf(STDOUT, "%s\n", {s})
    end if
end procedure

-- Check command-line arguments
sequence argv = command_line()
if length(argv) < 5 or length(argv[4]) = 0 or length(argv[5]) = 0
then
    usage()
end if

-- Parse 1st and 2nd command-line arguments
sequence arg_nums = {4, 5}
sequence lists = {}
for k = 1 to 2
do
    sequence list_result = parse_int_list(argv[arg_nums[k]])
    lists &= {list_result[PARSE_INT_LIST_VALUES]}
    if not list_result[PARSE_INT_LIST_VALID]
    then
        usage()
    end if
end for

-- Get longest common subsequence and display it
sequence result = longest_common_subsequence(lists[1], lists[2])
show_list_values(result)

```

{% endraw %}

Longest Common Subsequence in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
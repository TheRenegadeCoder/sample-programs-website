---
authors:
- rzuckerm
date: 2023-02-27
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2023-02-27
layout: default
tags:
- euphoria
- transpose-matrix
title: Transpose Matrix in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/euphoria/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
    puts(STDOUT, "Usage: please enter the dimension of the matrix and the serialized matrix\n")
    abort(0)
end procedure

-- Convert list of values to a matrix
function convert_to_matrix(sequence values, integer num_rows, integer num_cols)
    sequence matrix = repeat(repeat(0, num_cols), num_rows)
    integer count = 1
    for i = 1 to num_rows
    do
        matrix[i] = values[count..count + num_cols - 1]
        count += num_cols
    end for

    return matrix
end function

-- Transpose matrix
function transpose_matrix(sequence matrix)
    integer num_rows = length(matrix)
    integer num_cols = length(matrix[1])
    sequence matrix_t = repeat(repeat(0, num_rows), num_cols)
    for j = 1 to num_cols
    do
        matrix_t[j] = vslice(matrix, j)
    end for

    return matrix_t
end function

-- Show matrix as a list of comma-separated values
procedure show_matrix_as_list(sequence matrix)
    integer num_rows = length(matrix)
    integer num_cols = length(matrix[1])
    if num_rows > 0 and num_cols > 0
    then
        sequence format = repeat_pattern("%d, ", num_cols)
        sequence s = ""
        for i = 1 to num_rows
        do
            s &= sprintf(format, matrix[i])
        end for

        s = s[1..$-2]
        printf(STDOUT, "%s\n", {s})
    end if
end procedure

-- Check command-line arguments
sequence argv = command_line()
if (
    length(argv) < 6
    or length(argv[4]) = 0
    or length(argv[5]) = 0
    or length(argv[6]) = 0
)
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int(argv[4])
integer num_cols = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID] or num_cols < 0
then
    usage()
end if

-- Parse 2nd command-line argument
result = parse_int(argv[5])
integer num_rows = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID] or num_rows < 0
then
    usage()
end if

-- Parse 3rd command-line argument
result = parse_int_list(argv[6])
sequence values = result[PARSE_INT_LIST_VALUES]
integer num_values = length(values)
if not result[PARSE_INT_LIST_VALID] or num_values != num_rows * num_cols
then
    usage()
end if

-- Convert values to matrix
sequence matrix = convert_to_matrix(values, num_rows, num_cols)

-- Transpose matrix
sequence matrix_t = transpose_matrix(matrix)

-- Show transposed matrix as a list
show_matrix_as_list(matrix_t)

```

{% endraw %}

Transpose Matrix in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2023-02-25
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2023-02-25
layout: default
tags:
- euphoria
- maximum-array-rotation
title: Maximum Array Rotation in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/euphoria/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
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
    puts(STDOUT, "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")\n")
    abort(0)
end procedure

-- Find maximum array rotation, max{W(k), k=0..N-1}, where:
--
--     W(k) = sum{i*a[i+k mod N], i=0..N-1}
-- 
-- The value of W(k) can be calculated from W(k-1) as follows:
--
--     W(k) = W(k-1) - S + N*a[k-1]
--
-- where:
--
--     S = sum{a[i], i=0..N-1} = sum{a[i+x mod N], i=0..N-1}
--
-- where: x is any arbitary value
--
-- Proof:
--
-- - Set up initial assumption for W(k):
--
--     W(k-1) - S + N*a[k-1] = sum{i*a[i+k-1 mod N], i=0..N-1} - sum{a[i+k-1 mod N}, i=0..N-1} + N*a[k-1]
--
-- - Combine the two sums:
--
--     = sum{(i-1)*a[i+k-1 mod N], i=0..N-1} + N*a[k-1]
--
-- - Pull out the i=0 term:
--     = -a[k-1] + sum{(i-1)*a[i+k-1 mod N], i=1..N-1} + N*a[k-1]
--
-- - Combine the a[k-1] terms:
--
--     = sum{(i-1}*a[i+k-1 mod N], i=1..N-1) + (N-1)*a[k-1]
--
-- - Change indexing from i=1..N-1 to 0..N-2:
--
--     = sum{i*a[i+k mod N], i=0..N-2} + (N-1)*a[k-1]
--
-- - Bring the i=N-1 term back into the sum since N-1+k mod N equals k-1:
--
--     = sum{i*a[i+k mod N], i=0..N-1}
--
-- - The above equals W(k)
function maximum_array_rotation(sequence values)
    -- Calculate sum and initial array rotation
    integer s = 0
    integer w = 0
    integer n = length(values)
    for i = 1 to n
    do
        s += values[i]
        w += (i - 1) * values[i]
    end for

    -- Initialize maximum array rotation
    integer wmax = w

    -- Adjust array rotation and update maximum
    for i = 1 to n - 1
    do
        w += n * values[i] - s
        wmax = max({w, wmax})
    end for

    return wmax
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
if not result[PARSE_INT_LIST_VALID]
then
    usage()
end if

-- Find maximum array rotation and display result
integer value = maximum_array_rotation(values)
printf(STDOUT, "%d\n", value)

```

{% endraw %}

Maximum Array Rotation in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
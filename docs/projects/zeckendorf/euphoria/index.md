---
authors:
- rzuckerm
date: 2026-03-07
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-03-07
layout: default
tags:
- euphoria
- zeckendorf
title: Zeckendorf in Euphoria
title1: Zeckendorf
title2: in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/euphoria/how-to-implement-the-solution.md
- sources/programs/zeckendorf/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

procedure usage()
    puts(STDOUT, "Usage: please input a non-negative integer\n")
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

function get_fibonacci_values(integer value)
    -- Initialize Fibonacci state:
    -- fib(2) = 1
    -- fib(3) = 2
    sequence fibs = {}
    integer a = 1
    integer b = 2
    integer t

    -- Update Fibonacci state and store values
    while a <= value
    do
        -- fib(n) = fib(n - 1) + fib(n - 2)
        fibs &= a
        t = a + b
        a = b
        b = t
    end while

    return fibs
end function

function get_zeckendorf_values(integer value)
    sequence zecks = {}

    -- Go through Fibonacci numbers in reverse order, stopping when
    -- remaining value is zero
    sequence fibs = get_fibonacci_values(value)
    integer n = length(fibs)
    while n > 0 and value > 0
    do
        -- If candidate Fibonacci number is greater than or equal to remaining value,
        integer f = fibs[n]
        if value >= f
        then
            -- Append Fibonacci number to result
            zecks &= f

            -- Reduce remaining value
            value -= f

            -- Skip previous value
            n -= 2
        -- Else, go to previous value
        else
            n -= 1
        end if
    end while

    return zecks
end function

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int(argv[4])
integer value = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID] or value < 0
then
    usage()
end if

--Get Zeckendorf values
sequence values = get_zeckendorf_values(value)
show_list_values(values)

```

{% endraw %}

Zeckendorf in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2023-02-19
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-02-19
layout: default
tags:
- euphoria
- fibonacci
title: Fibonacci in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/euphoria/how-to-implement-the-solution.md
- sources/programs/fibonacci/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget

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
    puts(STDOUT, "Usage: please input the count of fibonacci numbers to output\n")
    abort(0)
end procedure

procedure show_fibonacci_values(integer value)
    -- Initialize Fibonacci state:
    -- fib(0) = 0
    -- fib(1) = 1
    integer a = 0
    integer b = 1
    integer t

    -- Update Fibonacci state and show results for requested number of values
    for n = 1 to value
    do
        -- fib(n) = fib(n - 1) + fib(n - 2)
        t = a + b
        a = b
        b = t

        printf(STDOUT, "%d: %d\n", {n, a})
    end for
end procedure

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int(argv[4])
integer value = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID]
then
    usage()
end if

-- Show requested number of Fibonacci values
show_fibonacci_values(value)

```

{% endraw %}

Fibonacci in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
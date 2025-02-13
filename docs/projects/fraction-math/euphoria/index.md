---
authors:
- rzuckerm
date: 2023-02-26
featured-image: fraction-math-in-every-language.jpg
last-modified: 2023-02-26
layout: default
tags:
- euphoria
- fraction-math
title: Fraction Math in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/euphoria/how-to-implement-the-solution.md
- sources/programs/fraction-math/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/math.e
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

-- Indices for parse_fraction() return value
enum NUM, DEN, PARSE_FRACTION_VALID

function parse_fraction(sequence s)
    -- Split numerator and denominator
    sequence parts = split(s, '/',, 2)

    -- Parse numerator
    sequence result = parse_int(parts[1])
    integer num = result[PARSE_INT_VALUE]
    boolean valid = result[PARSE_INT_VALID]

    -- Assume denominator is 1
    integer den = 1

    -- If numerator is valid and there is a denominator
    if valid and length(parts) > 1
    then
        -- Parse denominator
        result = parse_int(parts[2])
        valid = result[PARSE_INT_VALID]
        den = result[PARSE_INT_VALUE]
    end if

    return {num, den, valid}
end function

procedure usage()
    puts(STDOUT, "Usage: ./fraction-math operand1 operator operand2\n")
    abort(0)
end procedure

-- Do fraction math
function fraction_math(sequence fraction1, sequence op, sequence fraction2)
    object result
    switch op
    do
        case "+"
        then
            result = fraction_add(fraction1, fraction2)
        case "-"
        then
            result = fraction_sub(fraction1, fraction2)
        case "*"
        then
            result = fraction_mult(fraction1, fraction2)
        case "/"
        then
            result = fraction_div(fraction1, fraction2)
        case ">"
        then
            result = (fraction_compare(fraction1, fraction2) > 0)
        case ">="
        then
            result = (fraction_compare(fraction1, fraction2) >= 0)
        case "<"
        then
            result = (fraction_compare(fraction1, fraction2) < 0)
        case "<="
        then
            result = (fraction_compare(fraction1, fraction2) <= 0)
        case "=="
        then
            result = (fraction_compare(fraction1, fraction2) = 0)
        case "!="
        then
            result = (fraction_compare(fraction1, fraction2) != 0)
        case else
            printf(STDERR, "Invalid operator %s\n", {op})
    end switch

    return result
end function

-- Fraction reduction
function reduce(integer num, integer den)
    if den = 0
    then
        puts(STDERR, "Division by 0\n")
        abort(0)
    end if

    -- Reduce by dividing numerator and denominator by greatest common denominator,
    -- and adjust sign of numerator and denominator as follows:
    --
    -- n  d  sign n  sign d
    -- +  +     +       +
    -- +  -     -       +
    -- -  +     -       +
    -- -  -     +       +
    integer g = gcd(num, den)
    return {sign(den) * intdiv(num, g), intdiv(abs(den), g)}
end function

-- Fraction addition
-- n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1*d2)
function fraction_add(sequence fraction1, sequence fraction2)
    return reduce(
        fraction1[NUM] * fraction2[DEN] + fraction2[NUM] * fraction1[DEN],
        fraction1[DEN] * fraction2[DEN]
    )
end function

-- Fraction subtraction
-- n1/d1 + n2/d2 = (n1*d2 - n2*d1) / (d1*d2)
function fraction_sub(sequence fraction1, sequence fraction2)
    return reduce(
        fraction1[NUM] * fraction2[DEN] - fraction2[NUM] * fraction1[DEN],
        fraction1[DEN] * fraction2[DEN]
    )
end function

-- Fraction multiplication
-- n1/d1 * n2/d2 = (n1*n2) / (d1*d2)
function fraction_mult(sequence fraction1, sequence fraction2)
    return reduce(fraction1[NUM] * fraction2[NUM], fraction1[DEN] * fraction2[DEN])
end function

-- Fraction division
-- (n1/d1) / (n2/d2) = (n1*d2) / (n2*d1)
function fraction_div(sequence fraction1, sequence fraction2)
    return reduce(fraction1[NUM] * fraction2[DEN], fraction1[DEN] * fraction2[NUM])
end function

-- Fraction compare
-- n1/d1 OP n2/d2 = n1*d2 OP n2*d1
function fraction_compare(sequence fraction1, sequence fraction2)
    return fraction1[NUM] * fraction2[DEN] - fraction2[NUM] * fraction1[DEN]
end function

-- Show fraction result
procedure show_fraction_result(object result)
    -- If boolean, show boolean result
    if boolean(result)
    then
        printf(STDOUT, "%d\n", result)
    else
        printf(STDOUT, "%d/%d\n", {result[NUM], result[DEN]})
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

-- Parse 1st and 3rd command-line argument
sequence arg_nums = {4, 6}
sequence fractions = {}
for k = 1 to 2
do
    sequence result = parse_fraction(argv[arg_nums[k]])
    fractions &= {result[NUM..DEN]}
    if not result[PARSE_FRACTION_VALID]
    then
        usage()
    end if
end for

-- Parse 2nd command-line argument
sequence op = argv[5]

-- Do fraction math and show result
object fraction_result = fraction_math(fractions[1], op, fractions[2])
show_fraction_result(fraction_result)

```

{% endraw %}

Fraction Math in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
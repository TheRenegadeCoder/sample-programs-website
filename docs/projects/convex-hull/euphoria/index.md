---
authors:
- rzuckerm
date: 2023-02-25
featured-image: convex-hull-in-every-language.jpg
last-modified: 2023-03-27
layout: default
tags:
- convex-hull
- euphoria
title: Convex Hull in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/euphoria/how-to-implement-the-solution.md
- sources/programs/convex-hull/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/math.e
include std/mathcons.e

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
        "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. \"100, 440, 210\")\n"
    )
    abort(0)
end procedure

-- Indices of coordinates
enum X, Y

-- Combine values into a set of points
function form_points(sequence x_values, sequence y_values)
    integer n = length(x_values)
    sequence points = {}
    for k = 1 to n
    do
        points &= {{x_values[k], y_values[k]}}
    end for

    return points
end function

-- Find Convex Hull using Jarvis' algorithm
-- Source: https://www.geeksforgeeks.org/convex-hull-using-jarvis-algorithm-or-wrapping/
function convex_hull(sequence points)
    integer n = length(points)

    -- hull will be the set of points which form the convex hull
    -- Final set size is i
    sequence hull = {}

    -- The first point is the leftmost point with the highest y-coord in the
    -- event of a tie
    integer l = find_leftmost_point(points)

    -- Repeat until wrapped around to first hull point
    integer p = l
    integer q
    loop
    do
        -- Store convex hull point
        hull &= {points[p]}

        q = 1 + mod(p, n)
        for j = 1 to n
        do
            -- If point j is more counter-clockwise, then update end point (q)
            if orientation(points[p], points[j], points[q]) < 0
            then
                q = j
            end if
        end for

        p = q
    until p = l
    end loop

    return hull
end function

function find_leftmost_point(sequence points)
    integer n = length(points)
    atom min_x = PINF
    atom max_y = MINF
    integer min_index = 1
    integer x
    integer y
    for k = 1 to n
    do
        -- In the event of a tie, pick the point with the greater y-coord
        x = points[k][X]
        y = points[k][Y]
        if x < min_x or (x = min_x and y > max_y)
        then
            min_x = x
            max_y = y
            min_index = k
        end if
    end for

    return min_index
end function

-- Get orientation of three points
--
-- 0 = points are in a line
-- > 0 = points are clockwise
-- < 0 = points are counter-clockwise
function orientation(sequence p, sequence q, sequence r)
    return (
        (q[Y] - p[Y]) * (r[X] - q[X]) -
        (q[X] - p[X]) * (r[Y] - q[Y])
    )
end function

-- Show points
procedure show_points(sequence points)
    for k = 1 to length(points)
    do
        printf(STDOUT, "(%d, %d)\n", {points[k][X], points[k][Y]})
    end for
end procedure

-- Check 1st and 2nd command-line arguments
sequence argv = command_line()
if length(argv) < 5 or length(argv[4]) = 0 or length(argv[5]) = 0
then
    usage()
end if

-- Parse 1st and 2nd command-line arguments
sequence arg_nums = {4, 5}
sequence values = {}
for k = 1 to 2
do
    sequence result = parse_int_list(argv[arg_nums[k]])
    values &= {result[PARSE_INT_LIST_VALUES]}
    if not result[PARSE_INT_LIST_VALID] or length(values[k]) < 3
    then
        usage()
    end if
end for

-- Make sure same number of points
if length(values[1]) != length(values[2])
then
    usage()
end if

-- Combine values into set of points
sequence points = form_points(values[1], values[2])

-- Get convex hull of points and show points
sequence hull_points = convex_hull(points)
show_points(hull_points)

```

{% endraw %}

Convex Hull in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
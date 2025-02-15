---
authors:
- rzuckerm
date: 2023-01-29
featured-image: merge-sort-in-every-language.jpg
last-modified: 2023-01-31
layout: default
tags:
- algol68
- merge-sort
title: Merge Sort in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/algol68/how-to-implement-the-solution.md
- sources/programs/merge-sort/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
MODE PARSEINT_RESULT = STRUCT(BOOL valid, INT value, STRING leftover);
MODE PARSEINTLIST_RESULT = STRUCT(BOOL valid, REF []INT values);

PROC parse int = (REF STRING s) PARSEINT_RESULT:
(
    BOOL valid := FALSE;
    REAL r := 0.0;
    INT n := 0;
    STRING leftover;

    # Associate string with a file #
    FILE f;
    associate(f, s);

    # On end of input, exit if valid number not seen. Otherwise ignore it #
    on logical file end(f, (REF FILE dummy) BOOL:
        (
            IF NOT valid THEN done FI;
            TRUE
        )
    );

    # Exit if value error #
    on value error(f, (REF FILE dummy) BOOL: done);

    # Convert string to real number #
    get(f, r);

    # If real number is in range of an integer, convert to integer. Indicate integer is valid if same as real #
    IF ABS r <= max int
    THEN
        n := ENTIER(r);
        valid := (n = r)
    FI;

    # Get leftover string #
    get(f, leftover);

done:
    close(f);
    PARSEINT_RESULT(valid, n, leftover)
);

PROC count list items = (STRING s) INT:
(
    INT count := 1;
    FOR k TO UPB s
    DO
        IF s[k] = ","
        THEN
            count +:= 1
        FI
    OD;

    count
);

PROC parse int list = (REF STRING s) PARSEINTLIST_RESULT:
(
    BOOL valid := FALSE;
    STRING leftover := s;
    INT num list items = count list items(s);
    HEAP [num list items]INT values;

    # Repeat while valid value #
    FOR k TO num list items
    DO
        # Get next integer value and update leftover string #
        PARSEINT_RESULT result = parse int(leftover);
        valid := valid OF result;
        leftover := leftover OF result;

        # Append the integer value to list #
        values[k] := value OF result;

        # Do nothing if end of string #
        IF leftover = ""
        THEN
            SKIP
        # Skip comma if leftover string starts with comma #
        ELIF leftover[1] = ","
        THEN
            leftover := leftover[2:]
        # Otherwise indicate invalid #
        ELSE
            valid := FALSE
        FI
    UNTIL NOT valid
    OD;

    PARSEINTLIST_RESULT(valid, values)
);

PROC usage = VOID: (
    printf(($gl$, "Usage: please provide a list of at least two integers to sort in the format ""1, 2, 3, 4, 5"""))
);

COMMENT
Source: https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
COMMENT
PROC merge sort = (REF []INT values) VOID:
(
    # Create temporary work array and copy the values into it #
    INT n = UPB values;
    HEAP [n]INT working values := values;

    # Run the recursive merge sort #
    merge sort rec(working values, 1, n + 1, values)
);

PROC merge sort rec = (REF []INT working values, INT low, INT high, REF []INT values) VOID:
(
    # Only sort if enough values #
    IF (high - low) > 1
    THEN
        # Get midpoint #
        INT mid := (low + high) OVER 2;

        # Sort the left half (low to midpoint - 1) from values into working values #
        merge sort rec(values, low, mid, working values);

        # Sort the right half (midpoint to high - 1) from values into working values #
        merge sort rec(values, mid, high, working values);

        # Merge the two halves from working values into values #
        merge(working values, low, mid, high, values)
    FI
);

PROC merge = (REF []INT src, INT low, INT mid, INT high, REF []INT dest) VOID:
(
    # Copy the side that has the next largest value from the source to the destination #
    # until a side is exhausted #
    INT left index := low;
    INT right index := mid;
    INT combined index := low;
    INT len;
    WHILE left index < mid AND right index < high
    DO
        IF src[left index] <= src[right index]
        THEN
            dest[combined index] := src[left index];
            left index +:= 1
        ELSE
            dest[combined index] := src[right index];
            right index +:= 1
        FI;

        combined index +:= 1
    OD;

    # Copy the leftovers from the left side from the source to the destination #
    len := mid - left index;
    IF len > 0
    THEN
        dest[combined index:combined index + len - 1] := src[left index:mid - 1];
        combined index +:= len
    FI;

    # Copy the leftovers from the right side from the source to the destination #
    len := high - right index;
    IF len > 0
    THEN
        dest[combined index:combined index + len - 1] := src[right index:high - 1]
    FI
);

PROC show list values = (REF []INT values) VOID:
(
    INT n = UPB values;
    FOR k TO n
    DO
        IF k > 1
        THEN
            print(", ")
        FI;

        print(whole(values[k], 0))
    OD;

    IF n > 0
    THEN
        print(newline)
    FI
);

# Parse 1st command-line argument #
STRING s := argv(4);
PARSEINTLIST_RESULT list result := parse int list(s);
REF []INT values := values OF list result;
IF NOT valid OF list result OR UPB values < 2
THEN
    usage;
    stop
FI;

# Do merge sort and show results #
merge sort(values);
show list values(values)

```

{% endraw %}

Merge Sort in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
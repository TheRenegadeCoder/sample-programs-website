---
authors:
- rzuckerm
date: 2023-01-24
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2023-01-31
layout: default
tags:
- algol68
- palindromic-number
title: Palindromic Number in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/algol68/how-to-implement-the-solution.md
- sources/programs/palindromic-number/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
MODE PARSEINT_RESULT = STRUCT(BOOL valid, INT value, STRING leftover);

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

PROC usage = VOID: printf(($gl$, "Usage: please input a non-negative integer"));

PROC is palindromic number = (INT n) BOOL:
(
    # Convert number to string #
    STRING s := whole(n, 0);

    # Check if palindrome #
    INT len := UPB s;
    BOOL is palindrome := TRUE;
    FOR k TO len
    WHILE is palindrome
    DO
        is palindrome := (s[k] = s[len + 1 - k])
    OD;

    is palindrome
);

# Parse 1st command-line argument #
STRING s := argv(4);
PARSEINT_RESULT result := parse int(s);

# If invalid, extra characters, or negative, exit #
INT n := value OF result;
IF NOT (valid OF result) OR (leftover OF result) /= "" OR n < 0
THEN
    usage;
    stop
FI;

# Check if number is a palindrome and display results #
BOOL is palindrome := is palindromic number(n);
printf(($gl$, (is palindrome | "true" | "false")))

```

{% endraw %}

Palindromic Number in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
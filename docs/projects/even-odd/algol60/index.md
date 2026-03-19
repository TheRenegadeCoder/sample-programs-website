---
authors:
- rzuckerm
date: 2026-03-17
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-03-18
layout: default
tags:
- algol60
- even-odd
title: Even Odd in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/algol60/how-to-implement-the-solution.md
- sources/programs/even-odd/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin
    procedure usage;
    begin
        outstring(1, "Usage: please input a number\n");
        stop
    end usage;

    comment Input a digit character from stdin and return the following:
        - "0" to "9" maps to 0 to 9
        - "+" maps to 10
        - "-" maps to 11
        - whitespace maps to 12
        - comma maps to 13
        - null byte maps to -1
        - invalid bytes map to -2;
    integer procedure indigit;
    begin
        comment Mapping:
            - "0" to "9" maps to 1 to 10
            - "+" maps to 11
            - "-" maps to 12
            - "," mapps to 13
            - "\t" maps to 14
            - "\r" maps to 15
            - "\n" maps to 16
            - " " maps to 17
            - null byte maps to 18
            - invalid byte maps 0;
        integer ch;
        inchar(0, "0123456789+-,\t\r\n ", ch);
        if ch < 1 then ch := -2
        else if ch < 14 then ch := ch - 1
        else if ch < 18 then ch := 12
        else ch := -1;
        indigit := ch
    end indigit;

    comment Input an integer from stdin into 'result' and parse it.
        The last character is read into 'ch'.
        return true if integer is valid, false otherwise;
    boolean procedure inValidInteger(result, ch);
    integer result, ch;
    begin
        boolean valid;
        integer s;

        result := 0;
        valid := false;
        s := 1;

        comment Ignore whitespace;
        for ch := indigit while ch = 12 do;

        comment Process signs: ignore "+" and invert sign if "-";
    signloop:
        if ch = 10 | ch = 11 then
        begin
            if ch = 11 then s := -s;
            ch := indigit;
            goto signloop
        end;

        comment Process digits: update value;
    valueloop:
        if ch >= 0 & ch <= 9 then
        begin
            comment Invalid if overflow or underflow;
            valid := false;
            if (s > 0 & (maxint - ch) % 10 < result) |
                (s < 0 & (-1 - maxint + ch) % 10 > result) then goto done;

            result := result * 10 + s * ch;
            ch := indigit;
            valid := true;
            goto valueloop
        end;

        comment Ignore whitespace;
        for ch := ch while ch = 12 do ch := indigit;

    done:
        inValidInteger := valid
    end inValidInteger;

    boolean procedure iseven(x);
    value x;
    integer x;
    begin
        iseven := (x - 2 * (x % 2)) = 0
    end iseven;

    integer argc, result, ch;

    comment Get number of parameters. Exit if too few;
    ininteger(0, argc);
    if argc < 1 then usage;

    comment Get integer value from 1st argument. Exit if invalid or not
        end of argument;
    if !inValidInteger(result, ch) | ch != -1 then usage;

    comment Output "Even" if number is even, "Odd" otherwise;
    if iseven(result) then outstring(1, "Even")
    else outstring(1, "Odd")
end

```

{% endraw %}

Even Odd in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
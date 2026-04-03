---
authors:
- rzuckerm
date: 2026-04-01
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-04-03
layout: default
tags:
- algol60
- reverse-string
title: Reverse String in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/algol60/how-to-implement-the-solution.md
- sources/programs/reverse-string/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin
    integer procedure inAsciiChar;
    begin
        integer ch;

        comment
            To fix syntax highlighting on GitHub, use backslash x and:
            - 22 for double quote
            - 27 for single quote
            - 3b for semicolon
            For some reason percent sign needs to be represented as
            backslash x and 25;
        inchar(
            0,
            "\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f"
            "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
            " !\x22#$\x25&\x27()*+,-./0123456789:\x3b<=>?@ABCDEFGHIJKLMNO"
            "PQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f",
            ch
        );
        if ch >= 128 then ch := 0;
        inAsciiChar := ch
    end inAsciiChar;

    integer procedure inCharArray(s, maxLen);
    value maxLen;
    integer array s;
    integer maxLen;
    begin
        integer len, ch;

        len := 0;
    inloop:
        ch := inAsciiChar;
        if ch != 0 & len < maxLen then
        begin
            len := len + 1;
            s[len] := ch;
            goto inloop
        end;

        inCharArray := len
    end inCharArray;

    procedure outAsciiChar(ch);
    value ch;
    integer ch;
    begin
        comment
            To fix syntax highlighting on GitHub, use backslash x and:
            - 22 for double quote
            - 27 for single quote
            - 3b for semicolon
            For some reason percent sign needs to be represented as
            backslash x and 25;
        outchar(
            1,
            "\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f"
            "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
            " !\x22#$\x25&\x27()*+,-./0123456789:\x3b<=>?@ABCDEFGHIJKLMNO"
            "PQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f",
            ch
        )
    end outAsciiChar;

    procedure outCharArray(s, len);
    value len;
    integer array s;
    integer len;
    begin
        integer i;
        for i := 1 step 1 until len do outAsciiChar(s[i])
    end outCharArray;

    procedure reverseString(s, len);
    value len;
    integer array s;
    integer len;
    begin
        integer left, right, temp;

        left := 1;
        right := len;
    revloop:
        if left < right then
        begin
            temp := s[left];
            s[left] := s[right];
            s[right] := temp;
            left := left + 1;
            right := right - 1;
            goto revloop
        end
    end reverseString;

    integer argc, len;
    integer array s[1:256];

    comment Get number of parameters;
    ininteger(0, argc);

    comment If any parameters,;
    if argc > 0 then
    begin
        comment Get string as integer array;
        len := inCharArray(s, 256);

        comment Reverse string and output string as integer array;
        reverseString(s, len);
        outCharArray(s, len);
        if len > 0 then outstring(1, "\n")
    end
end

```

{% endraw %}

Reverse String in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
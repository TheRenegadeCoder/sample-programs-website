---
authors:
- rzuckerm
date: 2026-04-03
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-04-03
layout: default
tags:
- algol60
- longest-word
title: Longest Word in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/algol60/how-to-implement-the-solution.md
- sources/programs/longest-word/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin
    procedure usage;
    begin
        outstring(1, "Usage: please provide a string\n");
        stop
    end usage;

    integer procedure inAsciiChar;
    begin
        integer ch;

        comment
            To fix syntax highlighting on GitHub, use hex code for double quote and backtick.
            For some reason '%' needs to be represented as '\x25';
        inchar(
            0,
            "\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f"
            "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
            " !\x22#$\x25&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO"
            "PQRSTUVWXYZ[\\]^_\x60abcdefghijklmnopqrstuvwxyz{|}~\x7f",
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

    integer procedure longestWord(s, len);
    value len;
    integer array s;
    integer len;
    begin
        integer i, wordLen, maxWordLen, ch;

        wordLen := 0;
        maxWordLen := 0;
        for i := 1 step 1 until len do
        begin
            comment If whitespace, reset word length, else increment word length,
                and update maximum if necessary;
            ch := s[i];
            if ch = 9 | ch = 10 | ch = 13 | ch = 32 then wordLen := 0
            else
            begin
                wordLen := wordLen + 1;
                if wordLen > maxWordLen then maxWordLen := wordLen
            end
        end;

        longestWord := maxWordLen
    end longestWord;

    integer argc, len, maxWordLen;
    integer array s[1:256];

    comment Get number of parameters. Exit if too few;
    ininteger(0, argc);
    if argc < 1 then usage;

    comment Get string as integer array. Exit if empty;
    len := inCharArray(s, 256);
    if len < 1 then usage;

    comment Get maximum word length and output it;
    maxWordLen := longestWord(s, len);
    outinteger(1, maxWordLen);
    outstring(1, "\n")
end

```

{% endraw %}

Longest Word in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
authors:
- rzuckerm
date: 2025-03-28
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-28
layout: default
tags:
- algol68
- base64-encode-decode
title: Base64 Encode Decode in Algol68
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/algol68/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/algol68/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: (
    printf(($gl$, "Usage: please provide a mode and a string to encode/decode"))
);

STRING base64 chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[@0];
MODE DECODE_RESULTS = STRUCT(BOOL valid, STRING result);

PROC base64 encode = (STRING s) STRING:
(
    STRING result := "";
    INT s len = UPB s;
    BITS n1, n2, n3, u;
    FOR n BY 3 TO s len
    DO
        n1 := BIN ABS s[n];
        n2 := BIN (n + 1 <= s len | ABS s[n + 1] | 0);
        n3 := BIN (n + 2 <= s len | ABS s[n + 2] | 0);
        u := (n1 SHL 16) OR (n2 SHL 8) OR n3;
        result +:= base64 chars[ABS (u SHR 18)];
        result +:= base64 chars[ABS (u SHR 12 AND 16r3f)];
        result +:= (n + 1 <= s len | base64 chars[ABS (u SHR 6 AND 16r3f)] | "=");
        result +:= (n + 2 <= s len | base64 chars[ABS (u AND 16r3f)] | "=")
    OD;

    result
);

PROC base64 decode = (STRING s) DECODE_RESULTS:
(
    STRING result := "";
    INT s len := UPB s;
    INT pad count := count trailing pads(s);
    BOOL valid := s len MOD 4 = 0 AND pad count <= 2;

    INT n1, n2, n3, n4;
    BITS u;
    s len -:= pad count;
    FOR n BY 4 TO s len
    WHILE valid
    DO
        n1 := index of(s[n], base64 chars);
        n2 := index of(s[n + 1], base64 chars);
        n3 := (n + 2 <= s len | index of(s[n + 2], base64 chars) | 0);
        n4 := (n + 3 <= s len | index of(s[n + 3], base64 chars) | 0);
        valid := n1 >= 0 AND n2 >= 0 AND n3 >= 0 AND n4 >= 0;
        IF valid
        THEN
            u:= (BIN n1 SHL 18) OR (BIN n2 SHL 12) OR (BIN n3 SHL 6) OR BIN n4;
            result +:= REPR ABS (u SHR 16);
            result +:= (n + 2 <= s len | REPR ABS (u SHR 8 AND 16rff));
            result +:= (n + 3 <= s len | REPR ABS (u AND 16rff) | "")
        FI
    OD;

    DECODE_RESULTS(valid, result)
);

PROC count trailing pads = (STRING s) INT:
(
    INT s len := UPB s;
    INT n := s len;
    INT pad count := 0;
    WHILE n >= 1 AND n <= s len AND s[n] = "="
    DO
        pad count +:= 1;
        n -:= 1
    OD;

    pad count
);

PROC index of = (CHAR c, STRING s) INT:
(
    INT start index = LWB s;
    INT result := start index - 1;
    FOR n FROM start index TO UPB s
    WHILE result < start index
    DO
        IF s[n] = c
        THEN
            result := n
        FI
    OD;

    result
);

# Parse command-line arguments #
STRING mode := argv(4);
STRING s := argv(5);
IF UPB s = 0
THEN
    usage;
    stop
FI;

STRING result;
IF mode = "encode"
THEN
    result := base64 encode(s)
ELIF mode = "decode"
THEN
    DECODE_RESULTS decode result := base64 decode(s);
    IF NOT (valid OF decode result)
    THEN
        usage;
        stop
    FI;

    result := result OF decode result
ELSE
    usage;
    stop
FI;

printf(($gl$, result))

```

{% endraw %}

Base64 Encode Decode in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
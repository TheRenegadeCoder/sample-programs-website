---
title: Rot13 in Algol68
layout: default
date: 2023-01-24
featured-image: rot13-in-every-language.jpg
last-modified: 2023-01-24

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string to encrypt"));

PROC rot13 = (STRING s) STRING:
(
    INT code;
    STRING t;
    FOR n TO UPB s
    DO
        # If A-M or a-m, convert to N-Z or n-z by adding 13 to ASCII code #
        # Else, convert to A-M or a-m by subtracting 13 from ASCII code #
        code := ABS s[n];
        IF isalpha(s[n])
        THEN
            code +:= (tolower(s[n]) <= "m" | 13 | -13)
        FI;

        t +:= REPR code
    OD;

    t
);

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

# Encrypt string with ROT13 and display #
s := rot13(s);
printf(($gl$, s))
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Feb 01 2023 12:00:13. The solution was first committed on Jan 24 2023 12:24:28. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---
title: Duplicate Character Counter in Algol68
layout: default
date: 2023-01-22
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-01-22

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string"));

PROC duplicate character counter = (STRING s) REF []INT:
(
    # Initialize character counter #
    HEAP [0..255]INT char counter;
    FOR k FROM LWB char counter TO UPB char counter
    DO
        char counter[k] := 0
    OD;

    # Count number of occurances of each character #
    FOR k TO UPB s
    DO
        char counter[ABS s[k]] +:= 1
    OD;

    char counter
);

PROC show duplicate character counts = (STRING s, REF []INT char counter) VOID:
(
    BOOL has dupes := FALSE;
    INT code;
    FOR k TO UPB s
    DO
        code := ABS s[k];
        IF char counter[code] > 1
        THEN
            printf(($g": "gl$, s[k], whole(char counter[code], 0)));
            char counter[code] := 0;
            has dupes := TRUE
        FI
    OD;

    IF NOT has dupes
    THEN
        printf(($gl$, "No duplicate characters"))
    FI
);

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

# Count duplicate characters #
REF []INT char counter := duplicate character counter(s);

# Show all duplicate character counts in order in which they occurred in string (if any) #
show duplicate character counts(s, char counter)
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 31 2023 11:58:16. The solution was first committed on Jan 22 2023 14:02:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---

title: Duplicate Character Counter in Algol68
layout: default
date: 2022-04-28
last-modified: 2023-01-30

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string"));

# Command-line arguments start at 4. If too few, exit #
IF argc < 4
THEN
    usage;
    stop
FI;

# Get 1st command-line argument. Exit if empty #
STRING s := argv(4);
IF UPB s = 0
THEN
    usage;
    stop
FI;

# Initialize character counter #
[0..255]INT char counter;
FOR k FROM LWB char counter TO UPB char counter
DO
    char counter[k] := 0
OD;

# Count number of occurances of each character #
FOR k TO UPB s
DO
    char counter[ABS s[k]] +:= 1
OD;

# Show all duplicate character counts in order in which they occurred in string (if any) #
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
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
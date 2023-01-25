---

title: Reverse String in Algol68
layout: default
date: 2022-04-28
last-modified: 2023-01-25

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

CHAR temp;
INT len := UPB s;
FOR n TO len OVER 2
DO
    temp := s[len + 1 - n];
    s[len + 1 - n] := s[n];
    s[n] := temp
OD;

printf(($gl$, s))
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
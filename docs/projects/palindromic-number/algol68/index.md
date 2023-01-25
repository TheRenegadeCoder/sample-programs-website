---

title: Palindromic Number in Algol68
layout: default
date: 2022-04-28
last-modified: 2023-01-25

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
MODE PARSEINT_RESULT = STRUCT(BOOL valid, INT value, STRING leftover);
INT zero := ABS "0";

PROC find non blank = (STRING s, INT start) INT:
(
    INT pos := start;
    FOR k FROM pos TO UPB(s)
    WHILE isspace(s[k])
    DO
        pos +:= 1
    OD;

    pos
);

PROC parse int = (STRING s) PARSEINT_RESULT:
(
    BOOL valid := FALSE;
    INT sign := 1;
    REAL r := 0.0;
    INT n := 0;

    # Skip blanks #
    INT pos := find non blank(s, 1);

    # Handle sign #
    INT len := UPB(s);
    FROM pos TO len
    WHILE s[pos] = "+" OR s[pos] = "-"
    DO
        IF s[pos] = "-"
        THEN
            sign := -sign
        FI;

        pos +:= 1
    OD;

    # Convert the string to an integer until end-of-string or non-digit #
    FROM pos TO len
    WHILE isdigit(s[pos])
    DO
        valid := TRUE;
        r := r * 10.0 + (ABS s[pos]) - zero;
        pos +:= 1
    OD;

    # Make sure value is in range #
    r *:= sign;
    IF r < -(max int + 1.0) OR r > max int
    THEN
        valid := FALSE
    ELSE
        n := ENTIER(r)
    FI;

    pos := find non blank(s, pos);
    PARSEINT_RESULT(valid, n, s[pos:])
);

PROC usage = VOID: printf(($gl$, "Usage: please input a non-negative integer"));

# Command-line arguments start at 4. If too few, exit #
IF argc < 4
THEN
    usage;
    stop
FI;

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

# Convert number to string #
s := whole(n, 0);

# Check if palindrome #
INT len := UPB s;
BOOL is palindrome := TRUE;
FOR k TO len
WHILE is palindrome
DO
    is palindrome := (s[k] = s[len + 1 - k])
OD;

printf(($gl$, (is palindrome | "true" | "false")))
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
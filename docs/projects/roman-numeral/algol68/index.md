---
title: Roman Numeral in Algol68
layout: default
date: 2023-02-01
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2023-02-01

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC usage = VOID: printf(($gl$, "Usage: please provide a string of roman numerals"));
PROC error = VOID: printf(($gl$, "Error: invalid string of roman numerals"));

# Roman numeral table #
MODE ROMAN = STRUCT(CHAR letter, INT value);
[]ROMAN romans = (
    ("M", 1000),
    ("D", 500),
    ("C", 100),
    ("L", 50),
    ("X", 10),
    ("V", 5),
    ("I", 1)
);

# Get value of Roman letter #
PROC get roman = (CHAR letter) INT:
(
    INT value := 0;
    FOR k TO UPB romans
    WHILE value < 1
    DO
        IF (letter OF romans[k]) = letter
        THEN
            value := value OF romans[k]
        FI
    OD;

    value
);

# Convert Roman numeral to a value #
PROC roman number = (STRING s) INT:
(
    INT total := 0;
    INT prev value := -1; # No previous value #
    FOR k TO UPB s
    WHILE total >= 0
    DO
        # Get value of current letter. If not found, indicate invalid and exit #
        INT value := get roman(s[k]);
        IF value < 1
        THEN
            total := -1
        ELSE
            # Add value to total #
            total +:= value;

            # If there is a previous value and value is greater than previous value, #
            # subtract two times previous value from total to compensate for addition of #
            # previous value -- e.g., if previous value was 100 (C) and current value is #
            # 1000 (M), the total currently equals 1100, but we want it to be 900 (1100 - 2*100). #
            # Also, reset the current value so that there is no previous value #
            IF prev value > 0 AND value > prev value
            THEN
                total -:= 2 * prev value;
                value := -1
            FI;

            # Store current value to previous value #
            prev value := value
        FI
    OD;

    total
);
    
# If too few arguments, exit #
IF argc < 4
THEN
    usage;
    stop
FI;

# Convert Roman numeral to value #
STRING s := argv(4);
INT value := roman number(s);

# Display if valid, else show error message #
IF value >= 0
THEN
    printf(($gl$, whole(value, 0)))
ELSE
    error
FI
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
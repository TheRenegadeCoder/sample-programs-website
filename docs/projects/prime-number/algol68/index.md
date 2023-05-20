---
title: Prime Number in Algol68
layout: default
date: 2023-01-20
featured-image: prime-number-in-every-language.jpg
last-modified: 2023-01-20

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
MODE PARSEINT_RESULT = STRUCT(BOOL valid, INT value, STRING leftover);

PROC parse int = (REF STRING s) PARSEINT_RESULT:
(
    BOOL valid := FALSE;
    REAL r := 0.0;
    INT n := 0;
    STRING leftover;

    # Associate string with a file #
    FILE f;
    associate(f, s);

    # On end of input, exit if valid number not seen. Otherwise ignore it #
    on logical file end(f, (REF FILE dummy) BOOL:
        (
            IF NOT valid THEN done FI;
            TRUE
        )
    );

    # Exit if value error #
    on value error(f, (REF FILE dummy) BOOL: done);

    # Convert string to real number #
    get(f, r);

    # If real number is in range of an integer, convert to integer. Indicate integer is valid if same as real #
    IF ABS r <= max int
    THEN
        n := ENTIER(r);
        valid := (n = r)
    FI;

    # Get leftover string #
    get(f, leftover);

done:
    close(f);
    PARSEINT_RESULT(valid, n, leftover)
);

PROC usage = VOID: printf(($gl$, "Usage: please input a non-negative integer"));

PROC is prime = (INT n) BOOL:
(
    # If less than 2 or (not 2 and even), composite #
    # Else, check if prime by checking divisibility by odd numbers from 3 to sqrt(n) #
    BOOL prime := TRUE;
    IF n < 2 OR (n /= 2 AND n MOD 2 = 0)
    THEN
        prime := FALSE
    ELSE
        INT q := ENTIER(sqrt(n));
        INT k = 3;
        FOR k FROM 3 BY 2 TO q
        WHILE prime
        DO
            IF n MOD k = 0
            THEN
                prime := FALSE
            FI
        OD
    FI;

    prime
);

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

# Indicate if prime #
printf(($gl$, (is prime(n) | "Prime" | "Composite")))
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 30 2023 18:44:29. The solution was first committed on Jan 20 2023 11:12:25. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
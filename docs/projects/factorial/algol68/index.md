---
title: Factorial in Algol68
layout: default
date: 2023-01-21
featured-image: factorial-in-every-language.jpg
last-modified: 2023-01-21

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

# Allow answer to be up to 201 digits (googol squared!) #
PR precision=201 PR

PROC factorial = (INT n) LONG LONG INT:
(
    # Multiply from 1 through n (note that 0! = 1) #
    LONG LONG INT fact := 1;
    FOR k FROM 2 TO n
    DO
        # Exit if next multiplication will cause an overlow #
        IF fact > long long max int / k
        THEN
            putf(stand error, ($gl$, "Overflow!"));
            stop
        FI;

        fact *:= k
    OD;

    fact
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

# Calculate and display factorial #
LONG LONG INT fact := factorial(n);
print((whole(fact, 0), newline))
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 30 2023 18:32:37. The solution was first committed on Jan 21 2023 16:17:56. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
---

title: Fibonacci in Algol68
layout: default
date: 2022-04-28
last-modified: 2023-04-02

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
MODE PARSEINT_RESULT = STRUCT(BOOL valid, INT value, STRING leftover);
MODE PARSEINTLIST_RESULT = STRUCT(BOOL valid, REF []INT values);

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

PROC usage = VOID: printf(($gl$, "Usage: please input the count of fibonacci numbers to output"));

COMMENT
fib(n) = fib(n - 1) + fib(n - 2)
where:
- fib(0) = 0
- fib(1) = 1
COMMENT
MODE FIBSTATE = STRUCT(INT prev, INT result);
PROC init fib = FIBSTATE: FIBSTATE(0, 1);
OP FIB = (FIBSTATE state) FIBSTATE: (result OF state, prev OF state + result OF state);
OP FIBRESULT = (FIBSTATE state) INT: prev OF state;

PROC show fibonacci values = (INT n) VOID:
(
    # Initialize Fibonacci state #
    FIBSTATE state := init fib;

    # Update Fibonacci state and show results for requested number of values #
    FOR k TO n
    DO
        state := FIB state;
        printf(($g": "gl$, whole(k, 0), whole(FIBRESULT state, 0)))
    OD
);

# Parse 1st command-line argument #
STRING s := argv(4);
PARSEINT_RESULT result := parse int(s);

# If invalid or extra characters, exit #
INT n := value OF result;
IF NOT (valid OF result) OR (leftover OF result) /= ""
THEN
    usage;
    stop
FI;

# Show requested number of Fibonacci values #
show fibonacci values(n)
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 31 2023 21:23:22. The solution was first committed on Jan 21 2023 16:11:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
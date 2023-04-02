---

title: Factorial in Euphoria
layout: default
date: 2022-04-28
last-modified: 2023-04-02

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/math.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

procedure usage()
    puts(STDOUT, "Usage: please input a non-negative integer\n")
    abort(0)
end procedure

function factorial(integer value)
    -- Multiply from 1 through n (note that 0! = 1)
    atom fact = 1
    for n = 2 to value
    do
        -- Exit if next multiplication will cause an overlow
        fact *= n
        if not integer(fact)
        then
            puts(STDERR, "Overflow!\n")
            abort(0)
        end if
    end for

    return fact
end function

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int(argv[4])
integer value = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID] or value < 0
then
    usage()
end if

-- Calculate and display factorial
atom fact = factorial(value)
printf(STDOUT, "%d\n", {fact})
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
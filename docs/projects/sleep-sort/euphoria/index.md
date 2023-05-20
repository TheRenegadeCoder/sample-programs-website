---
title: Sleep Sort in Euphoria
layout: default
date: 2023-02-19
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2023-02-19

---

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/os.e

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

-- Indices for parse_int_list() return value
enum PARSE_INT_LIST_VALID, PARSE_INT_LIST_VALUES

function parse_int_list(sequence s)
    -- Split string on comma
    sequence list = split(s, ",")

    -- Parse each item
    integer valid = FALSE
    sequence values = {}
    for n = 1 to length(list)
    do
        sequence result = parse_int(list[n])
        valid = result[PARSE_INT_VALID]
        values &= result[PARSE_INT_VALUE]
        if not valid
        then
            exit
        end if
    end for

    return {valid, values}
end function

procedure usage()
    puts(
        STDOUT, 
        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n"
    )
    abort(0)
end procedure

procedure show_list_values(sequence values)
    if length(values) > 0
    then
        sequence format = repeat_pattern("%d, ", length(values))
        sequence s = sprintf(format[1..$-2], values)
        printf(STDOUT, "%s\n", {s})
    end if
end procedure

-- Although Euphoria claims to have a cooperative multi-tasking system,
-- I never could get this to work. Instead, just monitor the clock
-- and store values as each sleep time elapses
function sleep_sort(sequence sleep_times)
    -- Initialize values
    sequence values = {}

    -- Wait for all sleep times are complete
    atom start = time()
    while TRUE
    do
        -- For each sleep time that is not complete, when sleep time expires, append the
        -- sleep time to the list of values and remove the sleep time from the list
        atom current = time()
        sequence new_sleep_times = {}
        for k = 1 to length(sleep_times)
        do
            if (current - start) >= sleep_times[k]
            then
                values &= sleep_times[k]
            else
                new_sleep_times &= sleep_times[k]
            end if
        end for

        sleep_times = new_sleep_times
        if length(sleep_times) < 1
        then
            exit
        end if

        sleep(0.5)
    end while

    return values
end function

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int_list(argv[4])
sequence sleep_times = result[PARSE_INT_LIST_VALUES]
if not result[PARSE_INT_LIST_VALID] or length(sleep_times) < 2
then
    usage()
end if

-- Do sleep sort and show results
sequence values = sleep_sort(sleep_times)
show_list_values(values)
```

{% endraw %}

[Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Feb 26 2023 09:19:45. The solution was first committed on Feb 19 2023 22:01:49. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
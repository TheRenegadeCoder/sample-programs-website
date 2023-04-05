---

title: Roman Numeral in Euphoria
layout: default
date: 2022-04-28
last-modified: 2023-04-04

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e

procedure usage()
    puts(STDOUT, "Usage: please provide a string of roman numerals\n")
    abort(0)
end procedure

procedure error()
    puts(STDOUT, "Error: invalid string of roman numerals\n")
    abort(0)
end procedure

-- Roman numeral table
sequence romans = {
    {'M', 1000},
    {'D', 500},
    {'C', 100},
    {'L', 50},
    {'X', 10},
    {'V', 5},
    {'I', 1}
}

-- Indices for roman numeral table
enum ROMAN_LETTER, ROMAN_VALUE

-- Get value of Roman letter
function get_roman(integer letter)
    for k = 1 to length(romans)
    do
        if letter = romans[k][ROMAN_LETTER]
        then
            return romans[k][ROMAN_VALUE]
        end if
    end for

    return 0
end function

-- Convert Roman numeral to a value
function roman_number(sequence s)
    integer total = 0
    integer prev_value = -1 -- No previous value
    for k = 1 to length(s)
    do
        -- Get value of current letter. If not found, indicate invalid and exit
        integer value = get_roman(s[k])
        if value < 1
        then
            return -1
        end if

        -- Add value to total
        total += value

        -- If there is a previous value and value is greater than previous value,
        -- subtract two times previous value from total to compensate for addition of
        -- previous value -- e.g., if previous value was 100 (C) and current value is
        -- 1000 (M), the total currently equals 1100, but we want it to be 900 (1100 - 2*100).
        -- Also, reset the current value so that there is no previous value
        if prev_value > 0 and value > prev_value
        then
            total -= 2 * prev_value
            value = -1
        end if

        -- Store current value to previous value
        prev_value = value
    end for

    return total
end function

-- If too few arguments, exit
sequence argv = command_line()
if length(argv) < 4
then
    usage()
end if

-- Convert Roman numeral to value
sequence s = argv[4]
integer value = roman_number(s)
if value >= 0
then
    printf(STDOUT, "%d\n", {value})
else
    error()
end if
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
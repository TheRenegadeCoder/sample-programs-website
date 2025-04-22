---
authors:
- rzuckerm
date: 2025-04-22
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2025-04-22
layout: default
tags:
- awk
- roman-numeral
title: Roman Numeral in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/awk/how-to-implement-the-solution.md
- sources/programs/roman-numeral/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a string of roman numerals"
    exit(1)
}

function error() {
    print "Error: invalid string of roman numerals"
    exit(1)
}

function init_roman() {
    roman["I"] = 1
    roman["V"] = 5
    roman["X"] = 10
    roman["L"] = 50
    roman["C"] = 100
    roman["D"] = 500
    roman["M"] = 1000
}

function roman_numeral(s,  c, total, prev_value, value) {
    total = 0
    prev_value = -1 # No previous value
    for (i = 1; total >= 0 && i <= length(s); i++) {
        # Get value of current letter. If not found, error
        c = substr(s, i, 1)
        value = (c in roman) ? roman[c] : 0
        if (value < 1) {
            total = -1
        } else {
            # Add value to total value
            total += value

            # If there is a previous value and value is greater than previous value,
            # subtract two times previous value from total to compensate for addition of
            # previous value -- e.g., if previous value was 100 (C) and current value is
            # 1000 (M), the total currently equals 1100, but we want it to be 900 (1100 - 2*100).
            # Also, reset the current value so that there is no previous value
            if (prev_value > 0 && value > prev_value) {
                total -= 2 * prev_value
                value = -1
            }

            # Store current value to previous value
            prev_value = value
        }
    }

    return total
}

BEGIN {
    if (ARGC < 2) {
        usage()
    }

    init_roman()
    result = roman_numeral(ARGV[1])
    if (result >= 0) {
        print result
    } else {
        error()
    }
}

```

{% endraw %}

Roman Numeral in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
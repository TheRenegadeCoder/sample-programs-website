---
authors:
- rzuckerm
date: 2025-04-24
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-04-24
layout: default
tags:
- awk
- maximum-array-rotation
title: Maximum Array Rotation in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/awk/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")"
    exit(1)
}

function str_to_number(s) {
    return (s ~ /^\s*[+-]*[0-9]+\s*$/) ? s + 0 : "ERROR"
}

function str_to_array(s, arr,  str_arr, idx, result) {
    split(s, str_arr, ",")
    for (idx in str_arr) {
        result = str_to_number(str_arr[idx])
        if (result == "ERROR") {
            delete arr
            arr[1] = "ERROR"
            break
        } else {
            arr[idx] = result
        }
    }
}

function maximum_array_rotation(arr, n,  i, s, w, wmax) {
    # Calculate sum and initial array rotation
    for (i = 1; i <= n; i++) {
        s += arr[i]
        w += (i - 1) * arr[i]
    }

    # Initialize maximum array rotation
    wmax = w

    # Adjust array rotation and update maximum
    for (i = 1; i < n; i++) {
        w += n * arr[i] - s
        if (w > wmax) {
            wmax = w
        }
    }
    return wmax
}

BEGIN {
    if (ARGC < 2) {
        usage()
    }

    str_to_array(ARGV[1], arr)
    arr_len = length(arr)
    if (!arr_len || arr[1] == "ERROR") {
        usage()
    }

    result = maximum_array_rotation(arr, arr_len)
    printf("%d\n", result)
}

```

{% endraw %}

Maximum Array Rotation in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
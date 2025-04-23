---
authors:
- rzuckerm
date: 2025-04-23
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-04-23
layout: default
tags:
- awk
- maximum-subarray
title: Maximum Subarray in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/awk/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\""
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

function max(a, b) {
    return (a > b) ? a : b
}

# Find maximum subarray using Kadane's algorithm.
# Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted
function maximum_subarray(arr, n,  i, best_sum, current_sum) {
    # Awk doesn't have minus infinity, so use large negative number
    best_sum = -1e999
    current_sum = 0
    for (i = 1; i <=n ; i++) {
        current_sum = arr[i] + max(0, current_sum)
        best_sum = max(current_sum, best_sum)
    }

    return best_sum
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

    result = maximum_subarray(arr, arr_len)
    printf("%d\n", result)
}

```

{% endraw %}

Maximum Subarray in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
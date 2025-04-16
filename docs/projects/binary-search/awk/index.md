---
authors:
- rzuckerm
date: 2025-04-14
featured-image: binary-search-in-every-language.jpg
last-modified: 2025-04-16
layout: default
tags:
- awk
- binary-search
title: Binary Search in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/awk/how-to-implement-the-solution.md
- sources/programs/binary-search/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"
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

function is_sorted(arr, arr_len,  sorted, i) {
    sorted = 1
    for (i = 1; sorted && i < arr_len; i++) {
        sorted = (arr[i] <= arr[i + 1])
    }

    return sorted
}

function binary_search(arr, arr_len, target,  found, low, mid, high, value) {
    found = 0
    low = 1
    high = arr_len + 1
    while (low < high && !found) {
        mid = rshift(low + high, 1)
        value = arr[mid]
        if (value == target) {
            found = mid
        } else if (value < target) {
            low = mid + 1
        } else {
            high = mid
        }
    }

    return found
}

BEGIN {
    if (ARGC < 3) {
        usage()
    }

    str_to_array(ARGV[1], arr)
    target = str_to_number(ARGV[2])
    arr_len = length(arr)
    if (!arr_len || arr[1] == "ERROR" || target == "ERROR") {
        usage()
    }

    if (!is_sorted(arr, arr_len)) {
        usage()
    }

    idx = binary_search(arr, arr_len, target)
    print (idx > 0) ? "true" : "false"
}

```

{% endraw %}

Binary Search in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
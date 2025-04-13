---
authors:
- rzuckerm
date: 2025-04-07
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-04-07
layout: default
tags:
- awk
- linear-search
title: Linear Search in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/awk/how-to-implement-the-solution.md
- sources/programs/linear-search/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")"
    exit(1)
}

function str_to_number(s) {
    return (s ~ /^\s*[+-]*[0-9]+\s*$/) ? s + 0 : "ERROR"
}

function str_to_array(s, arr) {
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

function linear_search(arr, target) {
    result = 0
    for (idx in arr) {
        if (arr[idx] == target) {
            result = idx
            break
        }
    }

    return result
}

BEGIN {
    if (ARGC < 3) {
        usage()
    }

    str_to_array(ARGV[1], arr)
    target = str_to_number(ARGV[2])
    if (!length(arr) || arr[1] == "ERROR" || target == "ERROR") {
        usage()
    }

    idx = linear_search(arr, target)
    print (idx > 0) ? "true" : "false"
}

```

{% endraw %}

Linear Search in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
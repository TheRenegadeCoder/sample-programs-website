---
authors:
- Mykhaylo Samonov
- rzuckerm
date: 2019-10-20
featured-image: merge-sort-in-every-language.jpg
last-modified: 2023-07-25
layout: default
tags:
- groovy
- merge-sort
title: Merge Sort in Groovy
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/groovy/how-to-implement-the-solution.md
- sources/programs/merge-sort/groovy/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Groovy](https://sampleprograms.io/languages/groovy) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```groovy
class MergeSort {

    static sort(int[] data) { sort(data, 0, data.length - 1) }

    /**
     * Sorts the range data[start..end] in O(nlgn) time and O(n) space.
     */
    static sort(int[] data, int start, int end) {

        if (end > start) {

            int middle = (int) ((start + end) / 2)

            // Sort the left and right sides separately.
            sort(data, start, middle)
            sort(data, middle + 1, end)

            // Intertwine the data into one sorted list.
            mergeLists(data, start, middle, end)
        }

    }

    /**
     * Merges the two sorted sublists of data[start..middle] and data[middle+1..end].
     * O(n) time and memory.
     */
    static mergeLists(int[] data, int start, int middle, int end) {

        // Copy the left and right arrays because we'll be overwriting them.
        int[] left = Arrays.copyOfRange(data, start, middle+1)
        int[] right = Arrays.copyOfRange(data, middle+1, end+1)

        // Now, merge the lists by repeatedly adding the biggest value, from whichever list has it.
        int i = start, l = 0, r = 0 // l and r are indexes in left and right
        while (l < left.length && r < right.length)
            data[i++] = (left[l] <= right[r]) ? left[l++] : right[r++]

        // Add any leftovers on one side.
        while (l < left.length)
            data[i++] = left[l++]
        while (r < right.length)
            data[i++] = right[r++]
    }

    static int[] convert_to_ints(def args) {
        int[] argsint = []
        if (args?.size() >= 1) {
            try {
                argsint = args[0].split(",").collect { it.trim().toInteger() }
            }
            catch (NumberFormatException _) {
            }
        }

        argsint
    }

    public static void main(def args) {
        int[] argsint = convert_to_ints(args)
        if (argsint.size() < 2) {
            println 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'
        } else {
            sort(argsint) 
            println argsint
        }
    }

}
```

{% endraw %}

Merge Sort in [Groovy](https://sampleprograms.io/languages/groovy) was written by:

- Mykhaylo Samonov
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
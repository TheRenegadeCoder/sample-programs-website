---
authors:
- Jeremy Grifski
date: 2025-10-06
featured-image: selection-sort-in-every-language.jpg
last-modified: 2025-10-06
layout: default
tags:
- kotlin
- selection-sort
title: Selection Sort in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/kotlin/how-to-implement-the-solution.md
- sources/programs/selection-sort/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import kotlin.system.exitProcess

fun main(args: Array<String>) {
    val nums: IntArray = errorChecking(args)
    selectionSort(nums)
    outputList(nums)
}

fun usageError() {
    println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
}

fun errorChecking(args: Array<String>): IntArray {
    val nums: IntArray
    try {
        nums = args[0].split(", ").map { it.toInt() }.toIntArray()
    } catch (e: Exception) {
        usageError()
        exitProcess(1)
    }
    if (nums.size < 2) {
       usageError()
       exitProcess(1)
    }
    return nums
}

fun selectionSort(nums: IntArray) {
    for (i in 0 until nums.count() - 1) {
        
        var smallestIndex: Int = i
        for (j in i + 1 until nums.count()) {
            if (nums[j] < nums[smallestIndex]) {
                smallestIndex = j
            }
        }

        var swap: Int = nums[i]
        nums[i] = nums[smallestIndex]
        nums[smallestIndex] = swap
    }
}

fun outputList(nums: IntArray) {
    for (i in nums.indices) {
        if (i == nums.count() - 1) {
            println("${nums[i]}")
            return
        }
        print("${nums[i]}, ")
    }
}

```

{% endraw %}

Selection Sort in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
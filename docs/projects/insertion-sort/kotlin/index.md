---
authors:
- Jeremy Grifski
date: 2025-10-06
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2025-10-06
layout: default
tags:
- insertion-sort
- kotlin
title: Insertion Sort in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/kotlin/how-to-implement-the-solution.md
- sources/programs/insertion-sort/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import kotlin.system.exitProcess

fun main(args: Array<String>) {
    val nums: IntArray = errorChecking(args)
    insertionSort(nums)
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

fun insertionSort(nums: IntArray) {
    for (i in 1 until nums.count()) {
        val toMove: Int = nums[i]
        var j: Int = i - 1
        
        while (j >= 0 && nums[j] > toMove) {
            nums[j + 1] = nums[j]
            j = j - 1
        }
        
        nums[j + 1] = toMove
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

Insertion Sort in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).
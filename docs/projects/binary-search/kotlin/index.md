---
authors:
- Bolshialex
date: 2025-02-18
featured-image: binary-search-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- binary-search
- kotlin
title: Binary Search in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/kotlin/how-to-implement-the-solution.md
- sources/programs/binary-search/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args : Array<String>){
    if (args.size != 2) {
        println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
        return
    }

    val listInput = args[0].replace(",", "")
    val targetInput = args[1]

    val arr: IntArray
    val target: Int

    try {
        arr = listInput.split(" ").map { it.toInt() }.toIntArray()
        target = targetInput.toInt()
    } catch (e: NumberFormatException) {
        println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
        return
    }

    if (!isSorted(arr)) {
        println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
        return
    }

    val result = binarySearch(arr, target)
    println(result)
}

fun binarySearch(arr: IntArray, target: Int): Boolean{
    var left = 0;
    var right = arr.size - 1

    while(left <= right){
        var mid = (left + right) / 2;
        if(arr[mid] == target){
            return true
        } else if(arr[mid] < target){
            left = mid + 1
        }else{
            right = mid - 1
        }
    }
        
    return false
}


fun isSorted(arr: IntArray): Boolean {
    for (i in 0 until arr.size - 1) {
        if (arr[i] > arr[i + 1]) {
            return false
        }
    }
    return true
}
```

{% endraw %}

Binary Search in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Bolshialex

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).